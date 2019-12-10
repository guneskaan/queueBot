from slack import WebClient
from queue_bot import QueueBot

slack_bot_token = ''
web_client = {}

# Read Bot Token and Instantiate Slack WebClient.
try:
    with open(".SLACK_BOT_TOKEN") as token_file:
        for line in token_file:
            key, value = line.replace(" ","").partition("=")[::2]
            slack_bot_token = str(value).strip()

    web_client = WebClient(token=slack_bot_token)

except:
    sys.exit(" SLACK_BOT_TOKEN not found. \
    \n Please create a '.SLACK_BOT_TOKEN' file and set first line to 'SLACK_BOT_TOKEN = <SLACK_BOT_TOKEN>'")


# For simplicity we'll store our app data in-memory with the following data structure.
# active_queues = {"channel": queueBot}
active_queues = {}

def start_queueBot(channel: str):
    # Create a new queueBot instance.
    queueBot = QueueBot(channel)

    # Get the queueBot message payload
    message = queueBot.get_message_payload()

    # Post the queueBot message in Slack
    response = web_client.chat_postMessage(**message)

    # # Store the queueBot instance in active_queues
    # if channel not in active_queues:
    #     active_queues[channel] = {}
    active_queues[channel] = queueBot

def insert_queueBot(channel, user):
    if channel not in active_queues:
        return
    
    # Find the right active queue and insert new user
    queue = active_queues[channel]
    queue.insert_queue(user)

    # Get the updated queueBot message payload
    message = queue.get_message_payload()

    # Post the updated message in Slack
    updated_message = web_client.chat_update(**message)
    
