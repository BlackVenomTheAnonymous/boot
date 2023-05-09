Sure, here's an example code for a Telegram bot that responds to the `/bin` command with the corresponding BIN data using the API you provided:

```python
import requests
import telegram
from telegram.ext import CommandHandler, Updater

# Define the API endpoint and API key
API_ENDPOINT = 'https://api.bincodes.com/bin/'
API_KEY = '8f0e07e8765861bd21b2c54331c0c180'

# Define the emoji for the response
EMOJI = {
    'visa': '💳',
    'mastercard': '💳',
    'amex': '💳',
    'discover': '💳',
    'jcb': '💳',
    'diners': '💳',
    'maestro': '💳',
    'elo': '💳',
    'hipercard': '💳',
    'unionpay': '💳',
    'unknown': '❓',
}

# Define the handler for the /bin command
def bin_command(update, context):
    # Get the BIN number from the command arguments
    bin_number = context.args[0]

    # Call the API to get the BIN data
    response = requests.get(API_ENDPOINT, params={
        'format': 'json',
        'api_key': API_KEY,
        'bin': bin_number,
    })

    # Parse the response JSON
    data = response.json()

    # Get the card brand from the response
    brand = data.get('brand', 'unknown')

    # Get the emoji for the card brand
    emoji = EMOJI.get(brand.lower(), EMOJI['unknown'])

    # Build the response message
    message = f"{emoji} BIN {bin_number} belongs to {data.get('bank', {}).get('name', 'an unknown bank')} ({brand.upper()})"

    #Sure, here's an example code for a Telegram bot that responds to the `/uptime` command with the bot's uptime:

```python
import datetime
import telegram
from telegram.ext import CommandHandler, Updater

# Define the handler for the /uptime command
def uptime_command(update, context):
    # Get the bot's start time from the context
    start_time = context.bot_data.get('start_time')

    # Calculate the uptime
    uptime = datetime.datetime.now() - start_time

    # Build the response message
    message = f"The bot has been running for {uptime}"

    # Send the response message
    update.message.reply_text(message)

# Define the main function
def main():
    # Create an updater for the Telegram bot
    updater = Updater(token='5985008411:AAGskXRk_nbbzmY4knjhVUEV3dCNKiGd4nE', use_context=True)

    # Get the dispatcher for the updater
    dispatcher = updater.dispatcher

    # Register the /uptime command handler
    dispatcher.add_handler(CommandHandler('uptime', uptime_command))

    # Start the bot
    updater.start_polling()

    # Store the bot's start time in the bot data
    updater.bot_data['start_time'] = datetime.datetime.now()

    # Run the bot until it is stopped
    updater.idle()

# Call the main function
if __name__ == '__main__':
    main()
```

You will need to replace `5985008411:AAGskXRk_nbbzmY4knjhVUEV3dCNKiGd4nE` with your actual Telegram bot API token. Also, make sure to store the bot's start time in the `bot_data` dictionary so that it can be accessed by the `/uptime` command handler.
