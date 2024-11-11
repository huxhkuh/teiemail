
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# כאן נזין את הטוקן שלך
import os
TOKEN = os.getenv("TOKEN")


# פונקציה שמגדירה את התגובה לפקודת /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("שלום! אני כאן לעזור לך.")

# פונקציה שמגיבה לכל הודעת טקסט אחרת
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f"כתבת: {text}")

# הפונקציה הראשית שמריצה את הבוט
def main():
    application = Application.builder().token(TOKEN).build()

    # הוספת המאזין לפקודת /start
    application.add_handler(CommandHandler("start", start))

    # מאזין לכל הודעת טקסט
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # הפעלת הבוט
    application.run_polling()

if __name__ == '__main__':
    main()

