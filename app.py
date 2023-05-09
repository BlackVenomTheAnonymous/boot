import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set your Telegram bot token and channel username
telegram_token = os.environ['5985008411:AAF8uDeTiMKAzDZEOp5UzbnpRKpcbpVCCww']
channel_username = os.environ['likhon.anon']

# Define the Telegram API endpoint
telegram_api = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage'

# Define the start command handler
def start(update, context):
    # Get the chat ID from the user's message
    chat_id = update.message.chat_id
    
    # Check if the user has joined the channel
    is_member = context.bot.get_chat_member(channel_username, chat_id).status
    
    # If the user is not a member of the channel, send a message with a join link
    if is_member != 'member' and is_member != 'creator':
        message = "You must join our channel @" + channel_username + " to use this bot. Please join the channel and restart the bot.

Join our channel: https://t.me/" + channel_username + "

Once you have joined the channel, click the /start command to restart the bot."
        context.bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        return
    
    # If the user is a member of the channel, send a welcome message
    message = "Welcome to our bot! You can now use our bot's functionality."
    context.bot.send_message(chat_id=chat_id, text=message)

# Define the message handler
def message(update, context):
    # Get the chat ID and message text from the user's message
    chat_id = update.message.chat_id
    message_text = update.message.text
    
