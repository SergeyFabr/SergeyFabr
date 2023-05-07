import telebot
import random
import json
import os


token = "Your TOKEN"
bot = telebot.TeleBot(token)


def handler(event):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])
    return {
        'statusCode': 200,
        'body': "",
        }


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}!'
                     f'\nРад тебе😊'
                     f'\nЕсли ты здесь, значит хочешь получить подсказку на волнующую тему и я готов тебе в этом помочь.'
                     f'\n\nКак говорит Анна, все ответы всегда находятся внутри нас.'
                     f'\nВнимательно прочитай что нужно сделать:'
                     f'\n\n1. Произнеси вслух волнующий тебя вопрос.'
                     f'\n\nНапример, я хочу увеличить свой доход до 200 000 рублей в месяц.'
                     f'\n\n2. А теперь задай вопрос: какой мне нужно стать и что мне нужно сделать, чтобы ….'
                     f'(на месте точек твой запрос)'
                     f'\n\nНапример, какой мне нужно стать и что мне нужно сделать, чтобы мой доход в '
                     f'месяц составлял 200 000 рублей. '
                     f'\n\n3.Напиши свой запрос из пункта 2 сюда в чат👇🏻')


@bot.message_handler(content_types=['text'])
def send_text(message):
    choice_img = str(random.randint(1, 20)) + '.jpg'
    # img = "https://storage.yandexcloud.net/tg-bot-assistant-sanych/foto/" + choice_img # для работы на YandexCloud
    img = open(os.path.join('../Foto', choice_img), 'rb')
    if message.text.lower() == "получить карту":
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Подписаться на канал",
                                                        url="https://t.me/fabritckaya_anna")
        keyboard.add(url_button)
        bot.send_photo(message.chat.id, photo=img)
        bot.send_message(message.chat.id,
                         "Лови карту) Сейчас я помогу тебе ее проанализировать."
                         "\n\n1. Опиши вслух, что ты видишь на карте?"
                         "\n2. Какие чувства вызвала у тебя карта? "
                         "\n3. Как думаешь какую подсказку даёт тебе карта?"
                         "\n\n\nЧтобы оставаться на связи с Анной, подпишись на ее канал 👇🏻",
                         reply_markup=keyboard)
    else:
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard1.row('Получить карту')
        bot.send_message(message.chat.id, 'Хорошо. Видишь кнопку: «получить карту»? '
                                          'Нажни на нее и я достану для тебя из колоды карту-подсказку.',
                         reply_markup=keyboard1)