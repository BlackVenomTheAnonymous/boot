// Get the incoming webhook data
$data = file_get_contents('php://input');

// Parse the JSON data
$update = json_decode($data, true);

// Get the chat ID and message text from the incoming message
$chat_id = isset($update['message']['chat']['id']) ? $update['message']['chat']['id'] : '';
$message_text = isset($update['message']['text']) ? $update['message']['text'] : '';

// Perform the necessary actions based on the message data
if ($message_text == '/start') {
    // Send a welcome message to the user
    $message = "Welcome to my bot!";
    $params = [
        'chat_id' => $chat_id,
        'text' => $message,
    ];
    file_get_contents('https://api.telegram.org/bot<your-bot-token>/sendMessage?' . http_build_query($params
