mport telegram
import requests
from telegram.ext import CommandHandler, Updater

# Replace with your own API key
API_KEY = '8f0e07e8765861bd21b2c54331c0c180'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Bin Checker Bot! Send me a bin number to get started.")

def bin(update, context):
    bin_number = context.args[0]
    url = f'https://api.bincodes.com/bin/?format=json&api_key={API_KEY}&bin={bin_number}'
    response = requests.get(url)
    data = response.json()
    if data['valid']:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bin: {data['bin']} 
Brand: {data['brand']} 
Type: {data['type']}
Country: {data['country']}
Bank: {data['bank']}
Emoji: {data['emoji']}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid bin number. Please try again.")

def join(update, context):
    button = telegram.InlineKeyboardButton(text="Join Channel", url="https://t.me/likhon.anon")
    keyboard = [[button]]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Join our channel for more updates!", reply_markup=reply_markup)

def list_commands(update, context):
    commands = ['/start - Start the bot', '/bin [number] - Check bin data', '/join - Join our channel', '/list - List all commands', '/uptime - Check bot uptime']
    context.bot.send_message(chat_idHere's the code for the bot.py file that implements the requested features:

```python
import telegram
import requests
import os
import uptime
from telegram.ext import CommandHandler, Updater

# Replace with your own API key
API_KEY = '8f0e07e8765861bd21b2c54331c0c180'
# Replace with your own Telegram Bot API token
BOT_TOKEN = '5985008411:AAGskXRk_nbbzmY4knjhVUEV3dCNKiGd4nE'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Bin Checker Bot! Send me a bin number to get started.")

def bin(update, context):
    bin_number = context.args[0]
    url = f'https://api.bincodes.com/bin/?format=json&api_key={API_KEY}&bin={bin_number}'
    response = requests.get(url)
    data = response.json()
    if data['valid']:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bin: {data['bin']} 
Brand: {data['brand']} 
Type: {data['type']}
Country: {data['country']}
Bank: {data['bank']}
Emoji: {data['emoji']}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid bin number. Please try again.")

def join(update, context):
    button = telegram.InlineKeyboardButton(text="Join Channel", url="https://t.me/likhon.anon")
    keyboard = [[button]]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Join our channel for more updates!", reply_markup=reply_markup)

def list_commands(update
