from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext.filters import Text

# Токен вашего бота
TOKEN = "7207188394:AAFjvhmcxQhguacV5tnD_crOt8HDGh__lX4"

async def start(update: Update, context):
    """Обработчик команды /start."""
    await update.message.reply_text("Привет, я бот!")

async def reply_to_text(update: Update, context):
    """Обработчик текстовых сообщений."""
    text = update.message.text
    if "да" in text.lower():
        await update.message.reply_text("пизда")
    elif "короче" in text.lower() or "в общем" in text.lower():
        await update.message.reply_text("В сериале 'Как я встретил вашу маму' был точно такой же сюжет")
    else:
        await update.message.reply_text("Что-то другое")

def main():
    """Основная функция для запуска бота."""
    # Создаем объект Application
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Text & ~Text.command, reply_to_text))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
