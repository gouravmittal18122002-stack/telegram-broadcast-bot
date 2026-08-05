from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8224130351:AAEkkfYqVRbtqS6ELCMLR8I_vGDoT0jbkcg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Bot Ready! Aapka swagat hai.")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Aapne likha: {text}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, reply))

    print("Bot Ready ✅")
    app.run_polling()

if __name__ == "__main__":
    main()

