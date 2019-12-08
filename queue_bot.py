from queue import Queue
from collections import deque

class QueueBot:
    LINE_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to queueBot! :wave: \n\n"
                "*Here are the people in the line:*"
            ),
        },
        "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Line Up"
                        },
                        "action_id": "action_id",
                        "value": "view_alternate_2"
                    }
    }

    def __init__(self, channel):
        self.channel = channel
        self.username = "queueBot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.Q = deque()

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.LINE_BLOCK,
                self._get_queue_block()
            ],
        }

    def _get_queue_block(self):
        elements = list(map(usernameToBlockKitElement, self.Q))

        if not elements:
            return {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "There is no one in this queue yet! Click the \"Line Up\" button to be the first in the line!"
                }
            }

        return {
            "type": "context",
            "elements": elements
        }

    def insert_queue(self, username):
        if username not in self.Q:
            self.Q.append(username)

def usernameToBlockKitElement(username):
    return {
        "type": "plain_text",
        "text": username
    }
