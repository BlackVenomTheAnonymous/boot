import urllib2
import json

# Set your Telegram bot token and channel username
telegram_token = '5985008411:AAF8uDeTiMKAzDZEOp5UzbnpRKpcbpVCCww'
channel_username = 'likhon.anon'

# Define the Telegram API endpoint
telegram_api = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage'

# Get the chat ID and message text from the user's message
chat_id = message['chat']['id']
message_text = message['text']

# Check if the user has joined the channel
url = 'https://api.telegram.org/bot' + telegram_token + '/getChatMember?chat_id=' + channel_username + '&user_id=' + str(chat_id)
response = urllib2.urlopen(url)
data = json.load(response)
is_member = data['result']['status']

# If the user is not a member of the channel, send a message with a join link
if is_member != 'member' and is_member != 'creator':
    message = "You must join our channel @" + channel_username + " to use this bot. Please join the channel and restart the bot.

Join our channel: https://t.me/" + channel_username + "

Once you have joined the channel, click the /start command to restart the bot."
    params = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown',
    }
    urllib2.urlopen(telegram_api, urllib2.urlencode(params))
    return

# If the user is a member of the channel, continue with the bot's functionality
# ...
