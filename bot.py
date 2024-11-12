import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from upload_to_drive import upload_file_to_drive

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler
# ייבואים נוספים...

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

if not TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN environment variable is not set.")
    exit(1)

def send_email(subject, body):
    sender_email = "hahcvpurhoaphk@gmail.com"
    receiver_email =  "ll048123ll@gmail.com"
    password = os.environ.get('EMAIL_PASSWORD')

    if not password:
        print("Error: EMAIL_PASSWORD environment variable is not set.")
        return

    # יצירת הודעת המייל
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    # חיבור לשרת SMTP של Gmail ושליחת המייל
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)

# **הגדרת הפונקציה handle_message**
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    chat_id = update.message.chat_id
    sender_name = update.message.from_user.full_name

    # יצירת הנושא והתוכן של המייל
    subject = f"New message from {sender_name}"
    body = f"Chat ID: {chat_id}\nSender: {sender_name}\nMessage:\n{message_text}"

    # שליחת המייל
    send_email(subject, body)

    # אופציונלי: הדפסת לוג בקונסולה
    print(f"Email sent for message from {sender_name}")

# **הגדרת הפונקציה הראשית main**
def main():
    print("Starting bot...")
    app = ApplicationBuilder().token(TOKEN).build()

    # הוספת MessageHandler לטיפול בהודעות
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot is running...")
    app.run_polling()
    print("Bot stopped.")

if __name__ == '__main__':
    main()