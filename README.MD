# queueBot for Slack
Currently under development.
Requires `Python 3.6+`.

#### Setup and Development

1) Clone the repository to your working directory
2) Install dependencies
	```
	pip3 install -r requirements.txt
	```
3) Create a `.SLACK_BOT_TOKEN` file in the main directory and initialize `SLACK_BOT_TOKEN` on the first line to your `Bot User OAuth Access Token`:
	```
    SLACK_BOT_TOKEN = 'xoxb-XXXXXXXXXXXX-xxxxxxxxxxxx-XXXXXXXXXXXXXXXXXXXXXXXX'
    ```
	`Bot User OAuth Access Token` can be found on your application's `api.slack.com` page.

4) Similarly, create a `.OAUTH_ACCESS_TOKEN` file and initialize `OAUTH_ACCESS_TOKEN`:
	```
    OAUTH_ACCESS_TOKEN = 'xoxb-XXXXXXXXXXXX-xxxxxxxxxxxx-XXXXXXXXXXXX-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ```
	`OAuth Access Token` can be found on your application's `api.slack.com` page.

5) Go to `Your Apps` on `api.slack.com`, and select your application. Then go to `Interactive Components` and set the `Request Url` to your router's `IP Address`. <br><br> This way `Slack` will be able to send `HTTP Post` request on any interactions with `queueBot`'s messages (e.g button clicks).<br><br>NOTE: You might have to configure your router's settings to allow `HTTP` [port forwarding](https://whatismyipaddress.com/port-forwarding)<br><br> Learn more at [Creating interactive messages](https://api.slack.com/messaging/interactivity#components)

6) To be able to retreive profile pictures of users and display them in the queue, queueBot requires additional access scopes. In your applications page, go to `OAuth & Permissions` tab. Scroll down to the `Scopes` section, and click on `Add an OAuth Scope`. From the dropdown, find `users.profile:read` and add it to the list of scopes. A warning will appear on the page to reinstall the application in your organization.

7) Run the app
	```
    $ python3 app.py
	```
