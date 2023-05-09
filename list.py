import telegram
from telegram.ext import CommandHandler, Updater

# Define the function to handle the /list command
def list_commands(update, context):
    # List all available commands
    commands = ['/start', '/help', '/bin', '/list']
    response = "Available commands:
" + "
".join(commands)
    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Set up the Telegram bot
updater = Updater(token='5985008411:AAGskXRk_nbbzmY4knjhVUEV3dCNKiGd4nE', use_context=True)
dispatcher = updater.dispatcher

# Add the /list command handler
list_handler = CommandHandler('list', list_commands)
dispatcher.add_handler(list_handler)

# Start the bot
updater.start_polling()
