import telebot
bot = telebot.TeleBot(' ', parse_mode='MARKDOWN')
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, text="👋 Привет! Я бот Лицея №2! Здесь ты найдешь необходимые ссылки и интересную информацию.📄", reply_markup=markup)




@bot.message_handler(content_types=['text'])
def get_text_messages(message):


    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Ссылки на расписание📅')
        btn2 = types.KeyboardButton('Парламент⚖️')
        btn3 = types.KeyboardButton('Клубы и объединения🏠')
        btn4 = types.KeyboardButton('Выпускники🧑‍🎓')
        btn5 = types.KeyboardButton('Контактная информация☎️')
        markup.add(btn1, btn2, btn3, btn4,btn5)

        bot.send_message(message.from_user.id, text ='❗️Нажми, чтобы выбрать что-нибудь из меню:', reply_markup=markup) #ответ бота



    elif message.text == 'Ссылки на расписание📅':
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Таблица с расписанием🗒', url='https://docs.google.com/spreadsheets/d/1QX3Ak9YlUWiaIVEnC8V6GXzw0EIBBUnj/edit?usp=sharing&ouid=104153855704740100883&rtpof=true&sd=true')
        markup = types.InlineKeyboardMarkup()
        btn_my_bot = types.InlineKeyboardButton(text='Чат-бот с расписанием✈️', url='https://t.me/lyceum2perm_bot')
        markup.add(btn_my_site, btn_my_bot)

        bot.send_message(message.from_user.id, text = "❗️Выбери удобный для тебя формат❗️", reply_markup=markup)

    elif message.text == 'Парламент⚖️':
        inMurkup = types.InlineKeyboardMarkup(row_width=1)
        b2 = types.InlineKeyboardButton(text ="Министерство Культуры", callback_data='second')
        b1 = types.InlineKeyboardButton(text="Правительство", callback_data= 'first')
        b3 = types.InlineKeyboardButton(text="Министерство Образования👨🏻‍🏫", callback_data='thr')
        b4 = types.InlineKeyboardButton(text="Министерство Спорта", callback_data='fou')
        b5 = types.InlineKeyboardButton(text="Министерство Труда", callback_data='fif')
        b6 = types.InlineKeyboardButton(text="Министерство СМИ", callback_data='six')
        b7 = types.InlineKeyboardButton(text="Министерство Здравоохранения🏥", callback_data='sev')
        inMurkup.add(b1)
        inMurkup.add(b2)
        inMurkup.add(b3)
        inMurkup.add(b4)
        inMurkup.add(b5)
        inMurkup.add(b6)
        inMurkup.add(b7)

        bot.send_message(message.chat.id,  text="Выберите министерство:", reply_markup=inMurkup)

    elif message.text == 'Клубы и объединения🏠':
        club = types.InlineKeyboardMarkup()
        club1 = types.InlineKeyboardButton(text='Газета "Тихо!!!"🤫🔥', url='https://vk.com/thenewspaperlyceum')
        club = types.InlineKeyboardMarkup()
        club2 = types.InlineKeyboardButton(text='AVO Radio🎧', url='https://vk.com/radio_lyceum_2')
        club = types.InlineKeyboardMarkup()
        club3 = types.InlineKeyboardButton(text='Волонтерский Отряд🤝', url='https://vk.com/volunteers.lyceum2')
        club = types.InlineKeyboardMarkup()
        club4 = types.InlineKeyboardButton(text='Фотоцентр📸', url='https://vk.com/lnphotocenter')
        club = types.InlineKeyboardMarkup()
        club5 = types.InlineKeyboardButton(text='Киноклуб "Синемаголики"🎬', url='https://vk.com/lyceumcinemaholics')
        club = types.InlineKeyboardMarkup()
        club6 = types.InlineKeyboardButton(text='Интеллектуальный клуб🤓', url='https://vk.com/intellectual_club_lyceum')
        club = types.InlineKeyboardMarkup()
        club7 = types.InlineKeyboardButton(text='Дискусионный клуб👨‍⚖', url='https://vk.com/club214837647')
        club = types.InlineKeyboardMarkup()
        club8 = types.InlineKeyboardButton(text='Клуб настольных игр🎲', url='https://vk.com/public202272004')
        club = types.InlineKeyboardMarkup()
        club9 = types.InlineKeyboardButton(text='Speaking club🧐🇬🇧', url='https://vk.com/speakinclubl2')
        club = types.InlineKeyboardMarkup()
        club10 = types.InlineKeyboardButton(text='Команда КВН🎭', url='https://vk.com/kvnabok')
        club = types.InlineKeyboardMarkup()
        club11 = types.InlineKeyboardButton(text='Спортивный клуб⚽️', url='https://vk.com/club187186218')
        club = types.InlineKeyboardMarkup()
        club12 = types.InlineKeyboardButton(text='Литературный клуб🖊', url='https://vk.com/lyceumpoeticclub')
        club.add(club1)
        club.add(club2)
        club.add(club3)
        club.add(club4)
        club.add(club5)
        club.add(club6)
        club.add(club7)
        club.add(club8)
        club.add(club9)
        club.add(club10)
        club.add(club11)
        club.add(club12)
        bot.send_message(message.from_user.id, text="Выбери клуб или объединение и перейди по ссылке, чтобы узнать подробную информацию:", reply_markup=club)

    elif message.text == 'Выпускники🧑‍🎓':

        vip = types.InlineKeyboardMarkup()
        vip1 = types.InlineKeyboardButton("ФМ", callback_data='fm')
        vip = types.InlineKeyboardMarkup()
        vip2 = types.InlineKeyboardButton('МАТ', callback_data='mat')
        vip = types.InlineKeyboardMarkup()
        vip3 = types.InlineKeyboardButton("ИСТ", callback_data='ist')
        vip = types.InlineKeyboardMarkup()
        vip4 = types.InlineKeyboardButton("ХИМ", callback_data='him')
        vip = types.InlineKeyboardMarkup()
        vip5 = types.InlineKeyboardButton("ФИЛ", callback_data='fil')
        vip = types.InlineKeyboardMarkup()
        vip6 = types.InlineKeyboardButton("ЭК", callback_data='ek')
        vip.add(vip1, vip2, vip3)
        vip.add(vip4, vip5, vip6)
        bot.send_message(message.from_user.id, text ='Выбери класс выпускника:', reply_markup=vip)

    elif message.text == 'Контактная информация☎️':
        urls = types.InlineKeyboardMarkup()
        urls1 = types.InlineKeyboardButton(text='ВКонтакте', url='https://vk.com/lyc2perm')
        urls = types.InlineKeyboardMarkup()
        urls2 = types.InlineKeyboardButton(text='Зелёный диван', url='https://t.me/lyceumloungezone')
        urls = types.InlineKeyboardMarkup()
        urls3 = types.InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/@2-dj3go')
        urls = types.InlineKeyboardMarkup()
        urls4 = types.InlineKeyboardButton(text='Сайт', url='https://licey2perm.ru/')
        urls = types.InlineKeyboardMarkup()
        urls5 = types.InlineKeyboardButton(text='Old TikTok', url='https://www.tiktok.com/@lyceum_2?_t=8jIzmItPfUt&_r=1')
        urls = types.InlineKeyboardMarkup()
        urls6 = types.InlineKeyboardButton(text='New TikTok', url='https://www.tiktok.com/@lyceum2.0?_t=8jIznI19W5K&_r=1')
        urls.add(urls1, urls2, urls3, urls4, urls5, urls6)


        bot.send_message(message.from_user.id, text = '614089, Россия, Пермский край, г. Пермь, ул. Самаркандская, дом 102\n'
                                                      ' \n'
                                                      'Режим и график работы: Понедельник-пятница, с 9:00 до 17:30\n'
                                                      ' \n'
                                                      'Контактный телефон: 	+7(342) 282-43-42 (Приемная директора)\n'
                                                      '+7 (342) 281-95-61 (Заместитель директора по учебной работе)\n'
                                                      '+7 (342) 282-45-18 (Заместитель директора по воспитательной работе)\n'
                                                      ' \n'
                                                      'Email: licey2@permedu.online (Приемная директора)\n'
                                                      'Email: av.chepurin@yandex.ru (Директор)', reply_markup=urls)



@bot.callback_query_handler(func = lambda callback: True)
def check_callback_data(callback):
    if callback.data in 'first second thr fou fif six sev':
        if callback.data == 'first':
            bot.send_message(callback.message.chat.id, text = 'Все министерства работают под руководством правительства - оно контролирует работу всех органов Парламента, а также является связывающим звеном между администрацией Лицея и Лицеистами.')
        elif callback.data == 'second':
            bot.send_message(callback.message.chat.id, text='Министерство культуры организовывает культурно-массовые мероприятия Лицея, делает вашу жизнь ярче и интереснее.')
        elif callback.data == 'thr':
            bot.send_message(callback.message.chat.id, text = 'Министерство образования занимается организацией интеллектуальных игр, викторин, тематических недель.')
        elif callback.data == 'fou':
            bot.send_message(callback.message.chat.id,text='Министерство спорта занимается организацией спортивных турниров, а также динамичных мероприятий, проходящих на улице!')
        elif callback.data == 'fif':
            bot.send_message(callback.message.chat.id, text='Министерство труда помогает парламенту с оформлением мероприятий. Каждое лицейское событие становится уютнее и комфортнее с нашей помощью.')
        elif callback.data == 'six':
            bot.send_message(callback.message.chat.id,text='Министерство СМИ занимается созданием мультимедийного контента и информированием учащихся.')
        else:
            bot.send_message(callback.message.chat.id, text = 'Министерство здравоохранения отвечает за организацию встреч, посвященных медицине, работает совместно с отрядом волонтеров-медиков.')






bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

