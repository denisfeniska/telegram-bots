import telebot
from telebot import types

bot = telebot.TeleBot('5359524339:AAEHcH3WslV3cPHpRl38GKGyEBegoPTgDH8')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAIDxWITCaZnaUelQ0SNlHMTrjd2klAmAAIBAQACVp29CiK-nw64wuY0IwQ')
#    bot.send_message(chat_id=message.chat.id, text=message)
    mes = bot.send_message(chat_id=message.chat.id, text='Привет, big smoke\nТы зачем сюда пришёл?\nНаверное, '
                                                   'хочешь научиться телеграм ботов создавать')
    bot.register_next_step_handler(mes, sure)

def sure(message):
    if message.text.lower() == 'да':
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(chat_id=message.chat.id, text='<b>Ты уверен</b>\n/da\n/net', parse_mode='HTML')
    else:
        bot.send_message(chat_id=message.chat.id, text='Неправильный ответ, запускаю всё заново')
        start(message)


@bot.message_handler(commands=['net'])
def net(message):
    bot.send_message(chat_id=message.chat.id, text='Ну ладно')
    doc = open('telegram bots/different bots/stepik bot/tochno.txt')
    bot.send_document(chat_id=message.chat.id, document=doc)


@bot.message_handler(commands=['da'])
def da(message):
    kb = types.InlineKeyboardMarkup(row_width=3)
    da = types.InlineKeyboardButton(text='Да', callback_data='da')
    net1 = types.InlineKeyboardButton(text='Нет', callback_data='net1')
    net2 = types.InlineKeyboardButton(text='Нет', callback_data='net2')
    kb.add(da, net1, net2)
    bot.send_message(chat_id=message.chat.id, text='Подумай ещё раз', reply_to_message_id=message.message_id, reply_markup=kb)


@bot.callback_query_handler(func=lambda x: x.data)
def back(callback):
    kb = types.InlineKeyboardMarkup(row_width=3)
    da = types.InlineKeyboardButton(text='Да', callback_data='da')
    net1 = types.InlineKeyboardButton(text='Нет', callback_data='net1')
    net2 = types.InlineKeyboardButton(text='Нет', callback_data='net2')
    if callback.data == 'da':
        da1 = types.InlineKeyboardButton(text='Да', callback_data='da1')
        kb.add(net1, da1, net2)
        bot.edit_message_text(text='Подумай ещё раз', message_id=callback.message.message_id,
                              chat_id=callback.message.chat.id, reply_markup=kb)
    elif callback.data == 'da1':
        da2 = types.InlineKeyboardButton(text='Да', callback_data='da2')
        kb.add(net1, net2, da2)
        bot.edit_message_text(text='Подумай ещё раз', message_id=callback.message.message_id,
                              chat_id=callback.message.chat.id, reply_markup=kb)
    elif callback.data == 'da2':
        da3 = types.InlineKeyboardButton(text='Да', callback_data='da3')
        kb = types.InlineKeyboardMarkup(row_width=1)
        kb.add(da3, net1, net2)
        bot.edit_message_text(text='Подумай ещё раз', message_id=callback.message.message_id,
                              chat_id=callback.message.chat.id, reply_markup=kb)
    elif callback.data == 'da3':
        link = types.InlineKeyboardButton(text='Зайди сюда', url='https://7qp.github.io/telegram_bot/')
        kb.add(link)
        bot.edit_message_text(text='Хорошо', message_id=callback.message.message_id,
                              chat_id=callback.message.chat.id, reply_markup=kb)
    elif callback.data in ['net1', 'net2']:
        kb.add(net1, da, net2)
        bot.edit_message_text(text='Ок, пока', message_id=callback.message.message_id,
                              chat_id=callback.message.chat.id)


@bot.message_handler(content_types=['photo'])
def photo(message):
    pic = open('photo.jpg', 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=pic, caption='Ты почти у цели')
    mes = bot.send_message(chat_id=message.chat.id, text='Отправь свой ник в телеграмме')
    bot.register_next_step_handler(mes, finish)


def finish(message):
    if message.text == message.from_user.username:
        kb = types.InlineKeyboardMarkup()
        link = types.InlineKeyboardButton(text='Ссылка', url='https://stepik.org/lesson/667323/step/1?unit=665331')
        kb.add(link)
        bot.send_message(chat_id=message.chat.id, text='Добро пожаловать', reply_markup=kb)


bot.polling()