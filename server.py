from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import unquote
import json
from queues import start_queueBot, insert_queueBot

# Change logger setting to display INFO type messages.
logging.getLogger().setLevel(logging.INFO)

# Request Handler.
class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path), str(self.headers), post_data)
        
        if self.path == '/command':
            self.do_command(post_data)
            return

        # TODO: This codepath should only run for Slack interactive payloads.
        elif self.path == '/':
            key, payload = post_data.partition("=")[::2]
            # Replace escaped characters and parse JSON object.
            payload_json = json.loads(unquote(payload))

            insert_queueBot(payload_json["container"]["channel_id"], payload_json["user"])

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
    
    def do_command(self, post_data):
        pairs = post_data.split('&')
        pairsDict = dict(pair.split('=') for pair in pairs)
        start_queueBot(self, pairsDict["channel_id"], pairsDict["text"])

def start_server(server_class=HTTPServer, handler_class=Handler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    httpd.serve_forever()
