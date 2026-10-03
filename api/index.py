import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")


def telegram(method, data):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    return requests.post(url, json=data, timeout=10)


def main_menu():
    return {
        "keyboard": [
            ["💌 Открой, когда..."],
            ["❤️ Почему ты мне дорога", "🌸 Карточка дня"],
            ["🔮 Предсказание дня", "💌 Письма от меня"]
        ],
        "resize_keyboard": True
    }


@app.route("/", methods=["GET", "POST"])
@app.route("/api/index", methods=["GET", "POST"])
def webhook():

    if request.method == "GET":
        if request.args.get("setup") == "1":
            webhook_url = request.url.split("?")[0]

            result = telegram("setWebhook", {
                "url": webhook_url
            })

            return result.text

        return "Алина в кармане 💗 Бот работает!"


    update = request.get_json(silent=True)

    if not update:
        return "OK"


    message = update.get("message")

    if not message:
        return "OK"


    chat_id = message["chat"]["id"]
    text = message.get("text", "")


    if text == "/start":
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": (
                "Привет 💗\n"
                "Я — Алина в кармане.\n"
                "Маленькая версия Алины, которая теперь всегда рядом с тобой 🫂\n\n"
                "Здесь спрятаны мои мысли, поддержка и маленькие сюрпризы ✨"
            ),
            "reply_markup": main_menu()
        })

    elif text == "💌 Открой, когда...":
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "Выбери, когда хочешь открыть сообщение 💌"
        })

    elif text == "❤️ Почему ты мне дорога":
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "Здесь будет много причин, почему ты мне дорога ❤️"
        })

    elif text == "🌸 Карточка дня":
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "Твоя карточка дня 🌸"
        })

    elif text == "🔮 Предсказание дня":
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "Твоё предсказание 🔮"
        })

    elif text == "💌 Письма от меня":
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "Здесь будут мои письма тебе 💌"
        })

    else:
        telegram("sendMessage", {
            "chat_id": chat_id,
            "text": "Я пока не знаю, что ответить 🥺"
        })

    return "OK"
