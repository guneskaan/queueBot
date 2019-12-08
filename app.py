# TODO: Only import necessary methods
import os
import slack
import ssl as ssl_lib
import certifi
import sys
import socketserver
import logging
from queues import start_queueBot
from server import start_server
from threading import Thread

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the update_share callback to the 'message' event.

@slack.RTMClient.run_on(event="message")
def message(**payload):
    logging.info("Message payload Received,\nPayload: %s\n", str(payload))
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if text and text.lower() == "start":
        return start_queueBot(web_client, user_id, channel_id)

if __name__ == "__main__":
    slack_token = None
    
    try:
        with open(".SLACK_BOT_TOKEN") as token_file:
                for line in token_file:
                    key, value = line.replace(" ","").partition("=")[::2]
                    slack_token = str(value).strip()
    except:
        sys.exit(" SLACK_BOT_TOKEN not found. \
        \n Please create a '.SLACK_BOT_TOKEN' file and set first line to 'SLACK_BOT_TOKEN = <SLACK_BOT_TOKEN>'")

    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)

    # Start HTTP Server on a New Thread
    Thread(target = start_server, daemon = True).start()

    # Start Slack RTM Client
    rtm_client.start()
