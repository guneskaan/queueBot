from queue import Queue
from collections import deque
import logging

# Change logger setting to display INFO type messages
logging.getLogger().setLevel(logging.INFO)

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
        self.web_client = {}

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
        elements = list(map(userToBlockKitElement, self.Q))

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
            "elements": elements.insert(0, {
                "type": "mrkdwn",
                "text": ":one: : "
            })
        }

    def insert_queue(self, user):
        # TODO: Send appropriate error message if user is already in the queue
        if user in self.Q:
            logging.info('Error: User is already in the queue.')
            return

        self.Q.append(user)
        

def userToBlockKitElement(user):
    print("user is")
    print(user)
    print("user id is")
    print(user["id"])
    retrieved = self.web_client.users_profile_get(user = user["id"])
    print(retrieved)
    return {
        "type": "image",
        "image_url": retrieved["image_24"],
        "alt_text": user["name"]
    }
