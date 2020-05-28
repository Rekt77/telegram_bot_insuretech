import dialogflow_v2 as dialogflow
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logger = logging.getLogger()
logger.setLevel(logging.WARN)

TELEGRAM_TOKEN = '<your token id>'
project_id = "insurance-assistant-potoql"
session_id = "test-session-id"
language_code = "ko"

def googleSays(project_id, session_id, text, language_code):
    #session 생성
    session_client = dialogflow.SessionsClient()
    #session 생성
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    print(response.query_result.parameters)

    intent_name = response.query_result.intent.display_name
    googlesays = response.query_result.fulfillment_text
    

    return ({"intent_name":intent_name,"result":googlesays,"entities":[{}]})

def textMessage(update, bot):
    global session_id
    global project_id
    global language_code
    whatGoogleSays = googleSays(project_id, session_id, update.message.text, language_code)
    print(whatGoogleSays)
    update.message.reply_text(whatGoogleSays["result"])

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == "__main__":    
    """# Settings
    updater = Updater(token=TELEGRAM_TOKEN) # Telegram API Token
    dispatcher = updater.dispatcher"""

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, textMessage))

    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
        