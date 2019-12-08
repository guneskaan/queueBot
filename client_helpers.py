from slack import WebClient

oauth_access_token = ''

try:
    with open(".OAUTH_ACCESS_TOKEN") as token_file:
            for line in token_file:
                key, value = line.replace(" ","").partition("=")[::2]
                oauth_access_token = str(value).strip()
except:
    sys.exit(" OAUTH_ACCESS_TOKEN not found. \
    \n Please create a '.OAUTH_ACCESS_TOKEN' file and set first line to 'OAUTH_ACCESS_TOKEN = <OAUTH_ACCESS_TOKEN>'")
    
def fetchImageUrlForUserId(user_id):
    client = WebClient(token=oauth_access_token)
    response = client.users_profile_get(user = user_id)

    return unquote(response["profile"]["image_24"])
