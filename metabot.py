import telebot
from telebot import types

bot = telebot.TeleBot('')

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.surname = None
        self.age = None
        self.experience = None
        self.user_contact = None
        self.promo = None
        
        keys = ['promo', 'age', 'surname', 'experience', 'user_contact']
        for key in keys:
            self.key = None


@bot.message_handler(commands=['start'])
def prestarter(message):
    bot.send_message(1040492796, f'@{message.from_user.username} имя: {message.from_user.first_name} #{message.chat.id}')
    bot.send_message(message.chat.id, 'Добро пожаловать в Meta Academy 🚀')
    start(message)
            
def start(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    about_btn = types.KeyboardButton(text='ℹ️ О нас')
    webinar_btn = types.KeyboardButton(text='📘 Курсы')
    markup.add(about_btn, webinar_btn)
    
    bot.send_message(chat_id, 'Выбери действие ⏬', reply_markup=markup)
    bot.register_poll_handler(message, text)
    
@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    if message.text == 'ℹ️ О нас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        webinar_btn = types.KeyboardButton(text='✍🏻 Записаться на курс')
        about_btn = types.KeyboardButton(text='📞 Связаться')
        location_btn = types.KeyboardButton(text='📍 Локация')
        markup.add(menu_btn, about_btn, location_btn, webinar_btn)
        file = open('web.png', 'rb')
        bot.send_photo(chat_id, file,  '''Meta Academy - то, о чем тебе стоит знать.

Meta Academy является многопрофильным, авторизованным учебным центром, который предлагает узнать всё о криптовалюте.

Миссия академии - дать каждому из вас все знания, начиная с фундаментальных проектов и топовых NFT до участий в закрытых Pre-sale.

Мы выступаем за популяризацию цифровых активов и наши спикеры на протяжении 2-х лет активно изучают, анализируют рынок, проекты и новости. Тем самым, наши курсы всегда в топе актуальных событий.

Хочешь познать цифровой мир? Приходи учиться 😉''',
                                     reply_markup=markup)
        



        

    
    elif message.text == '⬅️ Назад':
        start(message)
        
    

    elif message.text == '✍🏻 Записаться на курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        pro_btn = types.KeyboardButton(text='🧬 PRO')
        basic_btn = types.KeyboardButton(text='🧬 Basic')
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        markup.add(pro_btn, basic_btn, menu_btn)
        bot.send_message(chat_id, 'Выбери курс', reply_markup=markup)
        
    elif message.text == '📞 Связаться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        webinar_btn = types.KeyboardButton(text='✍🏻 Записаться на курс')
        location_btn = types.KeyboardButton(text='📍 Локация')
        markup.add(menu_btn, webinar_btn, location_btn)
        bot.send_message(chat_id, 'Дмитрий - +998 90 947 16 57\nХусниддин - +998 90 091 09 05', reply_markup=markup)
        
    elif message.text == '📍 Локация':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        webinar_btn = types.KeyboardButton(text='✍🏻 Записаться на курс')
        about_btn = types.KeyboardButton(text='📞 Связаться')
        location_btn = types.KeyboardButton(text='📍 Локация')
        markup.add(menu_btn, about_btn, location_btn, webinar_btn)
        
        bot.send_location(chat_id, 41.3120340, 69.2910593, reply_markup=markup)
        
    elif message.text == '📘 Курсы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        pro_btn = types.KeyboardButton(text='🧬 PRO')
        basic_btn = types.KeyboardButton(text='🧬 Basic')
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        markup.add(pro_btn, basic_btn, menu_btn)
        bot.send_message(chat_id, 'Выбери курс', reply_markup=markup)
                       
    elif message.text == '🧬 PRO':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        reg_btn = types.KeyboardButton(text='🖌 Регистрация')
        basic_btn = types.KeyboardButton(text='🧬 Basic')

        markup.add(menu_btn, reg_btn, basic_btn)
        file_pro = open('pro.png', 'rb')
        bot.send_photo(chat_id, file_pro, '''
Курс для тех, кто хочет попробовать себя в новой сфере, интересно? Приходи на бесплатную лекцию, где ⤵️

✔️ откроешь для себя новые инструменты для пассивного дохода;
✔️ правильный разбор проектов и фондов;
✔️ возможности и скрытые инструменты.

Для посетителей бесплатной лекции будет приятный бонус 😉

''', reply_markup=markup)
        
    elif message.text == '🧬 Basic':
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu_btn = types.KeyboardButton(text='⬅️ Назад')
        reg_btn = types.KeyboardButton(text='🖌 Регистрация')
        pro_btn = types.KeyboardButton(text='🧬 PRO')
        markup.add(menu_btn, reg_btn, pro_btn)
        file_basic = open('basic.png', 'rb')
        bot.send_photo(chat_id, file_basic, ''' 
Meta Academy предоставляет тебе потрясающую возможность погрузиться в криптоиндустрию БЕСПЛАТНО 🤩

Регистрируясь на бесплатную лекцию ты узнаешь:

✔️ о криптограмотности;
✔️ почему уже сейчас стоит изучать мир криптовалюты;
✔️ отличие скамеров от фундаментальных проектов.

Для посетителей бесплатной лекции будет приятный бонус 😉''' , reply_markup=markup)
        
    elif message.text == '🖌 Регистрация':
        markup_remove = telebot.types.ReplyKeyboardRemove()
        bot.send_message(chat_id, 'Начнём!', reply_markup=markup_remove)
        reg(message)
        
    elif message.text == "✅ Завершить":
        chat_id = message.chat.id
        admin_id = 1040492796
        admin_id2 = 1911839691
        admin_id3 = 715001898
        admin_id4 = 329634508
        user_name = message.from_user.username
        user = user_dict[chat_id]
        bot.send_message(admin_id,  f'Новая заявка от @{user_name} \n'
                                    f' Имя: {user.name} \n'
                                    f' Фамилия: {user.surname} \n'
                                    f' Возраст: {user.age} \n'
                                    f' Опыт: {user.experience}\n'
                                    f' Промокод: {user.promo} \n'
                                    f' Номер: {user.user_contact} \n')
        
        bot.send_message(admin_id2, f'Новая заявка от @{user_name} \n'
                                    f' Имя: {user.name} \n'
                                    f' Фамилия: {user.surname} \n'
                                    f' Возраст: {user.age} \n'
                                    f' Опыт: {user.experience}\n'
                                    f' Промокод: {user.promo} \n'
                                    f' Номер: {user.user_contact} \n')
        
        bot.send_message(admin_id3, f'Новая заявка от @{user_name} \n'
                                    f' Имя: {user.name} \n'
                                    f' Фамилия: {user.surname} \n'
                                    f' Возраст: {user.age} \n'
                                    f' Опыт: {user.experience}\n'
                                    f' Промокод: {user.promo} \n'
                                    f' Номер: {user.user_contact} \n')
        
        bot.send_message(admin_id4, f'Новая заявка от @{user_name} \n'
                                    f' Имя: {user.name} \n'
                                    f' Фамилия: {user.surname} \n'
                                    f' Возраст: {user.age} \n'
                                    f' Опыт: {user.experience}\n'
                                    f' Промокод: {user.promo} \n'
                                    f' Номер: {user.user_contact} \n')        
        
        bot.send_message(chat_id, 'Регистрация завершена.\nВ скором времени наш менеджер свяжется с тобой.\nДо встречи 😉')
        start(message)
        
    elif message.text == '🔄 Заполнить заново':
        markup_remove = telebot.types.ReplyKeyboardRemove()
        bot.send_message(chat_id, 'Будь внимателен 😉', reply_markup=markup_remove)
        reg(message)
        
    elif message.text == '📂 Меню':
        start(message)
                
    else:
        bot.send_message(chat_id, 'Не верная команда!')
        start(message)
        
        
        
def admin(message):
    pasw = message.text
    if pasw == 'validwewe2001':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rasilka = types.KeyboardButton(text='Рассылка')
        markup.add(rasilka)
        bot.send_message(message.chat.id, 'успешно', reply_markup=markup)
    else:
        start(message)
        
        
def reg(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, '• Напиши имя: ')
    bot.register_next_step_handler(msg, name1)


def name1(message):
    name = message.text
    if name.isdigit():
        msg = bot.send_message(chat_id, '‼️Упсс... введи настоящее имя‼️')
        bot.register_next_step_handler(msg, reg)
        return
    chat_id = message.chat.id
    user = User(name)
    user_dict[chat_id] = user
    msg = bot.send_message(chat_id, '• Напиши фамилию: ')
    bot.register_next_step_handler(msg, surname1)
        

def surname1(message):
    surname = message.text
    if surname.isdigit():
        msg = bot.send_message(chat_id, '‼️Упсс... введи настоящую фамилию‼️')
        bot.register_next_step_handler(msg, name1)
        return
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.surname = surname
    msg = bot.send_message(chat_id, '• Сколько тебе лет? ')
    bot.register_next_step_handler(msg, age1)
        
        
def age1(message):
    chat_id = message.chat.id
    age = message.text
    if not age.isdigit():
        msg = bot.send_message(chat_id, '‼️Упсс... введи цифру‼️')
        bot.register_next_step_handler(msg, age1)
        return
    user = user_dict[chat_id]
    user.age = age
    msg = bot.send_message(chat_id, '• Был ли у тебя опыт в криптовалюте \ NFT?\n Если да, расскажи вкратце  ')
    bot.register_next_step_handler(msg, exp)
        
        
def exp(message):
    experience = message.text
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.experience = experience
    number_btn = types.KeyboardButton(text='📞 Поделится контактом', request_contact=True)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(number_btn)
    
   
    msg = bot.send_message(chat_id, '• Поделись контактными данными: ', reply_markup=markup)
    bot.register_next_step_handler(msg, promo)    

def promo(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    skip_btn = types.KeyboardButton(text='Пропустить')
    markup.add(skip_btn)
    chat_id = message.chat.id
    user_contact = message.contact.phone_number
    user = user_dict[chat_id]
    user.user_contact = user_contact
    msg = bot.send_message(chat_id, '• Напиши промокод: ', reply_markup=markup) 
    bot.register_next_step_handler(msg, check)
    
def check(message):
    if message.text == 'Пропустить':
        message.text = 'Без промокода'
    chat_id = message.chat.id
    promo = message.text
    user = user_dict[chat_id]
    user.promo = promo 
        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ready_btn = types.KeyboardButton(text='✅ Завершить')
    fill_again_btn = types.KeyboardButton(text='🔄 Заполнить заново')
    menu_btn = types.KeyboardButton(text='📂 Меню')
    markup.add(ready_btn,fill_again_btn,menu_btn)

    bot.send_message(chat_id,  '✅ Форма готова, проверь\n\n'
                                f'*Имя:* {user.name}\n'
                                f'*Фамилия:* {user.surname}\n'
                                f'*Возраст:* {user.age}\n'
                                f'*Опыт:* {user.experience}\n'
                                f'*Номер:* {user.user_contact}\n'
                                f'*Промокод:* {user.promo}', reply_markup=markup, parse_mode='MarkDown')
    bot.register_next_step_handler(message, text)


bot.polling(non_stop=True)