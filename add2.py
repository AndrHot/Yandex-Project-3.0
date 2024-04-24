from telebot import TeleBot, types

bot = TeleBot("6938592889:AAG3lk3iwpOG1ag-wHvkyU5wEH0sfLbclSo")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 6):
        button = types.InlineKeyboardButton(str(i), callback_data=f"test_{i}")
        markup.add(button)
    bot.send_message(message.chat.id, "Выберите номер кнопки:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("test_"):
        bot.answer_callback_query(call.id)
        start(call.message)
        button_num = call.data.split("_")[1]


bot.polling()
