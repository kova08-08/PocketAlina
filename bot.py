import telebot
from telebot import types

TOKEN = "8676263246:AAEc28Ikr6yPVONBrSUQYds8FUj-WrVgNnk"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("💌 Открой, когда...")
    btn2 = types.KeyboardButton("❤️ Почему ты мне дорога")
    btn3 = types.KeyboardButton("🌸 Карточка дня")
    btn4 = types.KeyboardButton("🔮 Предсказание дня")
    btn5 = types.KeyboardButton("💌 Письма от меня")

    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)

    bot.send_message(
        message.chat.id,
        "Привет 💗\n"
        "Я — Алина в кармане.\n"
        "Маленькая версия Алины, которая теперь всегда рядом с тобой 🫂\n\n"
        "Здесь спрятаны мои мысли, поддержка и маленькие сюрпризы ✨",
        reply_markup=markup
    )


bot.infinity_polling()
