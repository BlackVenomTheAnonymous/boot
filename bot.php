import requests
from pyrogram import Client, filters
from configs import config
from asyncio import sleep

from pyrogram.types import (
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)

Bot = Client(
    ":memory:",
    api_hash=config.API_HASH,
    api_id=config.API_ID,
    bot_token=config.BOT_TOKEN,
)

@Bot.on_message(filters.command("start"))
async def start(_, m: Message):
    messy = m.from_user.mention
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Channel", url="https://t.me/likhon_anon"),
                InlineKeyboardButton("Support", url="https://t.me/likhon_anon"),
            ],
            ],
        ]
    )
    await m.reply_text(
        f"Hi! {messy} 
I can Check bins Valid or Invalid.

To see more check /help command",
        reply_markup=keyboard,
    )

@Bot.on_message(filters.command("help"))
async def help(_, m: Message):
    await m.reply_text(
        "/start - To check bot alive.
/help - **To see help menu.**
/bin [qoury] - To check Bin is valide or Invalid."
    )

@Bot.on_message(filters.command("bin"))
async def bin(_, m: Message):
    if len(m.command) < 2:
        msg = await m.reply_text("Please Provide a Bin!
Ex:- /bin 401658")
        await sleep(15)
        await msg.delete()
    else:
        try:
            mafia = await m.reply_text("processing...")
            inputm = m.text.split(None, 1)[1]
            bincode = 
Here's an example code for forcing users to join a Telegram channel before they can use the bot:
<?php // Set your Telegram bot token and channel username $telegram_token = '5985008411:AAF8uDeTiMKAzDZEOp5UzbnpRKpcbpVCCww'; $channel_username = 'likhon_anon'; // Define the Telegram API endpoint $telegram_api = 'https://api.telegram.org/bot' . $telegram_token . '/sendMessage'; // Get the chat ID and message text from the user's message $chat_id = isset($message['chat']['id']) ? $message['chat']['id'] : ''; $message_text = isset($message['text']) ? $message['text'] : ''; // Check if the user has joined the channel $is_member = json_decode(file_get_contents("https://api.telegram.org/bot$telegram_token/getChatMember?chat_id=$channel_username&user_id=$chat_id"), true)['result']['status']; // If the user is not a member of the channel, send a message with a join link if ($is_member != 'member' && $is_member != 'creator') { $message = "You must join our channel $channel_username to use this bot. Please join the channel and restart the bot."; $message .= " Join our channel: https://t.me/$channel_username"; $message .= " Once you have joined the channel, click the /start command to restart the bot."; $params = [ 'chat_id' => $chat_id, 'text' => $message, 'parse_mode' => 'Markdown', ]; file_get_contents($telegram_api . '?' . http_build_query($params)); exit; } // If the user is a member of the channel, send a welcome message and instructions on how to use the bot $message = "Welcome to our bot! Here are some commands you can use: /bin [BIN number] - Get information
<?php
// Set your Telegram bot token and channel username
$telegram_token = '5985008411:AAF8uDeTiMKAzDZEOp5UzbnpRKpcbpVCCww';
$channel_username = 'likhon_anon';

// Define the Telegram API endpoint
$telegram_api = 'https://api.telegram.org/bot' . $telegram_token . '/sendMessage';

// Get the chat ID and message text from the user's message
$chat_id = isset($message['chat']['id']) ? $message['chat']['id'] : '';
$message_text = isset($message['text']) ? $message['text'] : '';

// Check if the user has joined the channel
$is_member = json_decode(file_get_contents("https://api.telegram.org/bot$telegram_token/getChatMember?chat_id=$channel_username&user_id=$chat_id"), true)['result']['status'];

// If the user is not a member of the channel, send a message with a join link
if ($is_member != 'member' && $is_member != 'creator') {
    $message = "You must join our channel $channel_username to use this bot. Please join the channel and restart the bot.";
    $message .= "

Join our channel: https://t.me/$channel_username";
    $message .= "

Once you have joined the channel, click the /start command to restart the bot.";
    $params = [
        'chat_id' => $chat_id,
        'text' => $message,
        'parse_mode' => 'Markdown',
    ];
    file_get_contents($telegram_api . '?' . http_build_query($params));
    exit;
}

// If the user is a member of the channel, continue with the bot's functionality
// ...

This code checks if the user has joined the specified Telegram channel using the getChatMember API<?php
// Set your Telegram bot token and API key
$telegram_token = '5985008411:AAF8uDeTiMKAzDZEOp5UzbnpRKpcbpVCCww';
$api_key = '8f0e07e8765861bd21b2c54331c0c180';

// Define the Telegram API endpoint
$telegram_api = 'https://api.telegram.org/bot' . $telegram_token . '/sendMessage';

// Get the bin number from the user's message
$bin = isset($message['text']) ? trim(str_replace('/bin', '', $message['text'])) : '';

// Make the API request to get the bin data
$url = 'https://api.bincodes.com/bin/?format=json&api_key=' . $api_key . '&bin=' . $bin;
$response = file_get_contents($url);
$data = json_decode($response, true);

// Prepare the message to send back to the user
if ($data && isset($data['country'])) {
    $message = "🌍 Country: " . $data['country']['name'] . " (" . $data['country']['alpha2'] . ")
";
    $message .= "💳 Card Type: " . $data['card']['type'] . "
";
    $message .= "💰 Bank: " . $data['bank']['name'] . "
";
    $message .= "🏢 Bank URL: " . $data['bank']['url'] . "
";
    $message .= "📞 Bank Phone: " . $data['bank']['phone'] . "
";
    $message .= "
    button = InlineKeyboardButton("Likhon Sheikh", url="https://t.me/likhon_anon")
} else {
    $message = "Sorry, we couldn't find any data for that bin number.";
}

// Send the message back to the user
$chat_id = isset
<?php
