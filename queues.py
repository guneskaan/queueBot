from slack import WebClient
from queue_bot import QueueBot

# For simplicity we'll store our app data in-memory with the following data structure.
# active_queues = {"channel": queueBot}
active_queues = {}

def start_queueBot(web_client: WebClient, user_id: str, channel: str):
    # Create a new queueBot instance.
    queueBot = QueueBot(channel)

    # Get the queueBot message payload
    message = queueBot.get_message_payload()

    # Post the queueBot message in Slack
    response = web_client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    queueBot.timestamp = response["ts"]

    # Store the WebClient object in queueBot for future communications
    queueBot.web_client = web_client

    # # Store the queueBot instance in active_queues
    # if channel not in active_queues:
    #     active_queues[channel] = {}
    active_queues[channel] = queueBot

def insert_queueBot(channel: str, username: str):
    if channel not in active_queues:
        return
    
    # Find the right active queue and insert new user
    queue = active_queues[channel]
    queue.insert_queue(username)

    # Get the updated queueBot message payload
    message = queue.get_message_payload()

    # Post the updated message in Slack
    updated_message = queue.web_client.chat_update(**message)
    
