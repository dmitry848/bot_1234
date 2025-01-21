from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен вашего бота от BotFather
TOKEN = "7207188394:AAFjvhmcxQhguacV5tnD_crOt8HDGh__lX4"

# Настройки ключевых слов и ответов
RESPONSES = {
    "да": "пизда",
    "короче": "В сериале 'Как я встретил вашу маму' был точно такой же сюжет",
    "в общем": "В сериале 'Как я встретил вашу маму' был точно такой же сюжет",
}


# Обработка текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    # Получаем текст сообщения
    message_text = update.message.text.lower()  # Приводим текст к нижнему регистру
    for key_word, response in RESPONSES.items():
        if key_word in message_text:  # Если ключевое слово найдено в сообщении
            update.message.reply_text(response)
            break  # Отвечаем только один раз на сообщение

# Главная функция
def main():
    # Создаем Updater с вашим токеном
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    updater.idle()

# Запуск кода
if __name__ == "__main__":
    main()
