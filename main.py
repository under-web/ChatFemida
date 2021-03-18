from telebot import apihelper

import telebot
import time
from config import bot_token

# PROXY = 'socks5://195.78.112.235:42549'
# apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(bot_token)
keyboard_one = telebot.types.ReplyKeyboardMarkup(True)
keyboard_one.row('Да я предприниматель', 'Не Являюсь таковым')

keyboard_two = telebot.types.ReplyKeyboardMarkup(True)
keyboard_two.row('Мне уже есть 21 год', 'Еще не исполнилось 21 год')
keyboard_two.row('Мне больше 45 лет')

keyboard_three = telebot.types.ReplyKeyboardMarkup(True)
keyboard_three.row('Нет судимостей', 'Да, есть судимость')

keyboard_thor = telebot.types.ReplyKeyboardMarkup(True)
keyboard_thor.row('Нет задолженностей', 'Есть долг')

keyboard_five = telebot.types.ReplyKeyboardMarkup(True)
keyboard_five.row('Есть гражданство РФ', 'Нет гражданства РФ')

keyboard_six = telebot.types.ReplyKeyboardMarkup(True)
keyboard_six.row('Казань', 'РТ')
keyboard_six.row('Нет, я из другого региона')


# my_id = 1107191282

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    img = open('money.jpg', 'rb')
    bot.send_photo(message.chat.id, img)

    info = """
    Юридическая компания предлагает дополнительный заработок за 14 дней!!!🔥🔥🔥
              
    Мы готовим новые компании с расчётными счётами 
    для дальнейшего переоформления на покупателя,
    через нотариальную контору( договор купли-продажи).
    Без рисков,все в рамках закона РФ 💼
    
    Пройдите короткий опрос.⤵️
              
    Являетесь ли вы зарегистрированным руководителем 
    или индивидуальным предпринимателям сейчас или
    за последние 3 года?
           """
    bot.send_message(message.chat.id, info, reply_markup=keyboard_one)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Не Являюсь таковым':
        bot.send_message(message.chat.id, 'Хорошо! Ваш возраст от 21 до 45 ?',
                         reply_markup=keyboard_two)
    elif message.text == 'Да я предприниматель':
        del_k = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'К сожалению вы нам не подходите, но вы можете порекомендовать знакомым и '
                                          'неплохо на этом заработать '
                                          '\nЧтобы начать сначала введите  /start', reply_markup=del_k)
    elif message.text == 'Мне уже есть 21 год':
        bot.send_message(message.chat.id, 'Имеется ли у вас судимость в том числе непогашенная?',
                         reply_markup=keyboard_three)
    elif message.text == 'Мне больше 45 лет':
        del_keb = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'К сожалению вы нам не подходите, но вы можете порекомендовать знакомым и '
                                          'неплохо на этом заработать',
                         reply_markup=del_keb)

    elif message.text == 'Еще не исполнилось 21 год':
        del_ke = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'К сожалению вы нам не подходите, но вы можете порекомендовать знакомым и '
                                          'неплохо на этом заработать',
                         reply_markup=del_ke)
    elif message.text == 'Нет судимостей':
        bot.send_message(message.chat.id, 'Отлично! Имеется ли у вас задолженность ФССП?',
                         reply_markup=keyboard_thor)
    elif message.text == 'Нет задолженностей':
        bot.send_message(message.chat.id, 'Вы гражданин РФ?',
                         reply_markup=keyboard_five)
    elif message.text == 'Есть гражданство РФ':
        bot.send_message(message.chat.id, 'Место жительства город Казань или РТ?',
                         reply_markup=keyboard_six)
    elif message.text == 'Нет, я из другого региона':
        del_l = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'К сожалению вы нам не подходите, но вы можете порекомендовать знакомым и '
                                          'неплохо на этом заработать '
                                          '\nЧтобы начать сначала введите  /start', reply_markup=del_l)
    elif message.text == 'Казань':

        del_key = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Отлично! Вы нам подходите!🎉🎉🎉 \n\nОставьте свой номер телефона '
                                          '(через +7), а так же ваше Имя🎫📫📝\n\n''Мы с вами свяжемся в кратчайшее '
                                          'время!!!',
                         reply_markup=del_key)
    elif message.text == 'РТ':

        del_key = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Отлично! Вы нам подходите!🎉🎉🎉 \n\nОставьте свой номер телефона '
                                          '(через +7), а так же ваше Имя🎫📫📝\n\n''Мы с вами свяжемся в кратчайшее '
                                          'время!!!',
                         reply_markup=del_key)

    elif 7 and '+' in message.text:
        with open('контакты.txt', 'a', encoding='utf-8') as text_file:
            text_file.writelines(message.text + '\n')
        bot.send_message(message.chat.id, 'Отлично! Будьте на связи!👍📞💲')
        bot.send_message(1641211276, message.text) # мой айди
        bot.send_message(1580963189, message.text) # айди куда слать клиенту
    else:
        del_kyb = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Введите пожалуйста корректные данные номер телефона (ЧЕРЕЗ +7)\nЧтобы начать сначала введите  /start', reply_markup=del_kyb)

    # bot.polling(none_stop=True, interval=1)


while True:
    print('Я Работаю v.2.0.1')

    try:
        bot.polling(none_stop=True, interval=3, timeout=20)
        print('Этого не должно быть')
        # bot.infinity_polling(True)
        # proc = os.getpid()
        # time.sleep(60)
        # os.kill(proc, signal.SIGTERM)

    except telebot.apihelper.ApiException:
        print('Проверьте связь и API')
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
