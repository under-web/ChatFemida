import telebot
import time
from config import bot_token

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
keyboard_six.row('Я живу в Казани', 'Я живу в другом городе')


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
              
    Являетесь ли вы руководителем 
    или индивидуальным предпринимателям?
           """
    bot.send_message(message.chat.id, info, reply_markup=keyboard_one)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Да я предприниматель':
        bot.send_message(message.chat.id, 'Хорошо! Ваш возраст от 21 до 45 ?',
                         reply_markup=keyboard_two)
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
        bot.send_message(message.chat.id, 'Место жительства город Казань?',
                         reply_markup=keyboard_six)
    elif message.text == 'Я живу в Казани':
        del_key = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Отлично! Вы нам подходите!🎉🎉🎉 \n\nОставьте свой номер телефона '
                                          '(через +7), а так же ваше Имя🎫📫📝\n'
                                          'Или можете позвонить нам сами для получения '
                                          'остальной информации\n\n'
                                          '+7 950 314 85 15',
                         reply_markup=del_key)
    elif not 'Мне больше 45 лет' and '+7' or '+' in message.text:
        with open('контакты.txt', 'a', encoding='utf-8') as text_file:
            text_file.writelines(message.text + '\n')
        bot.send_message(message.chat.id, 'Ваши контакты отправлены!')
    else:
        del_kyb = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'К сожалению вы нам не подходите, но вы можете порекомендовать знакомым и '
                                          'неплохо на этом заработать '
                                          '\nЧтобы начать сначала введите  /start', reply_markup=del_kyb)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(10)
