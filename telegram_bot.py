import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import requests
import json

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
async def chatgpt(message):
    api_url = "https://api.openai.com/v1/chat/completions"

# Set the API key (replace YOUR_API_KEY with your actual API key)
    token=""
    api_key = "Bearer "+token

# Set the request parameters
    data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": message}],
    "temperature": 0.7
    }

# Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }

# Send the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Extract the response JSON content
    response_data = response.json()
    print(response_data)
    print(type(response_data))
    return response_data['choices'][0]['message']['content']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    # message_text = await chatgpt(message_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Response: \n {message_text}")

if __name__ == '__main__':
    token_string=""
    application = ApplicationBuilder().token(token_string).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT & (~ filters.COMMAND), reply_to_message)
    application.add_handler(message_handler)

    application.run_polling()
