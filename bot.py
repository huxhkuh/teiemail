from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# כאן נזין את הטוקן שלך
TOKEN = '7772604825:AAH3eIkicj4EDI7I6pF_rLRXDnxzuK5iGsU'

# פונקציה שמגדירה את התגובה לפקודת /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("שלום! אני כאן לעזור לך.")

# פונקציה שמגיבה לכל הודעת טקסט אחרת
def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(f"כתבת: {text}")

# הפונקציה הראשית שמריצה את הבוט
def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # הוספת המאזין לפקודת /start
    dispatcher.add_handler(CommandHandler("start", start))

    # מאזין לכל הודעת טקסט
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # הפעלת הבוט
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
