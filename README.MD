# queueBot for Slack
Currently under development.
Requires `Python 3.6+`.

#### Setup and Development

1) Clone the repository to your working directory
2) Install dependencies
	```
	pip3 install -r requirements.txt
	```
3) Set your `SLACK_BOT_TOKEN` environment variable to your `Bot User OAuth Access Token` found on your application's `api.slack.com` page.
	```
    $ export SLACK_BOT_TOKEN='xoxb-XXXXXXXXXXXX-xxxxxxxxxxxx-XXXXXXXXXXXXXXXXXXXXXXXX'
    ```
4) Go to `Your Apps` on `api.slack.com`, and select your application. Then go to `Interactive Components` and set the `Request Url` to your `IP Address`. This way `Slack` will be able to send `HTTP Post` request on any interactions with `queueBot`'s messages (e.g button clicks). <br> Learn more at [Creating interactive messages](https://api.slack.com/messaging/interactivity#components)

5) Run the app
	```
    $ python3 app.py
	```
