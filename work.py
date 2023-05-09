import os
from telegram.ext import CommandHandler, Updater
from bot import start, bin, join, list_commands, uptime

# Replace with your own Telegram Bot API token
BOT_TOKEN = '5985008411:AAGskXRk_nbbzmY4knjhVUEV3dCNKiGd4nE'

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    bin_handler = CommandHandler('bin', bin)
    join_handler = CommandHandler('join', join)
    list_handler = CommandHandler('list', list_commands)
    uptime_handler = CommandHandler('uptime', uptime)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(bin_handler)
    dispatcher.add_handler(join_handler)
    dispatcher.add_handler(list_handler)
    dispatcher.add_handler(uptime_handler)

    # Start the bot
    updater.start_polling()
    print('Bot is running!')
    updater.idle()

if __name__ == '__main__':
    main()
