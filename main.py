import telebot
from telebot import types


bot = telebot.TeleBot('7475281032:AAGbxQqSbLQohYpAY5M7_C1hQ2h7gBOQju8')

@bot.message_handler(commands=['import'])
def Mimport(message):
    bot.send_message(message.chat.id, 'Весь список произведений бота:')
    for i in texts:
        bot.send_message(message.chat.id,i)

@bot.message_handler(commands=['start', 'main', 'hello'])
def handle_start_main_hello(message):
    bot.send_message(message.chat.id,
    f'{message.from_user.first_name}, встречайте!\n<b>Book Bot</b> - это <b>новейший</b> телеграм бот,для генерации кратких содержаний популярных произведений.'
    f'\nИспользуйте /import, чтобы узнать библиотеку бота.\nВажное уточнение!Аудио файлы будут доступны только на школьные произведения и на некоторых других.'
    f'\nПосмотреть другие работы автора, поддержать: http://127.0.0.1:8000/ (сайт не работает всегда, если вы хотите посетить его, пожалуйста, свяжитесь со мной: @OffZarLine)'
    f'\nНапишите название произвидения для генерации краткого содержания (/import):', parse_mode='html')

texts = ['Джордж Оруэлл - 1984', 'Джек Лондон - Белый Клык', 'Чак Паланик - Бойцовский Клуб', 'Фрэнсис Скотт Ки Фицджеральд - Великий Гэтсби',
         'Эрих Мария Ремарк - На Западном фронте без перемен', 'Денис Фонвизин - Недоросль', 'Александр Пушкин - Капитанская дочка, Пиковая дама',
         'Беляев Александр - Человек-амфибия', 'Александр Пушкин - Белые ночи', 'Иван Тургенев - Первая любовь, Ася', 'Джонатан Сфивт - Путешествия Гулливера',
         'Герберт Уэллс - Машина времени, Человек-невидимка', 'Михаил Лермонтов - Мцыри', 'Гоголь - Шинель, Ревизор',
         'Михаил Шолохов — Судьба человека','Лев Толстой - Отрочество', 'Михаил Булгаков - Собачье сердце', 'Васильев Борис - А зори здесь тихие',
         'Уильям Шекспир - Ромео и Джульетта', 'Александр Солженицын - Матренин двор', 'Мольер - Мещанин Во Дворянстве', 'Эрих Мария Ремарк - Три товарища',
         'Эрих Ремарк - На обратном пути', 'Чак Паланик - Колыбельная', 'Джордж Оруэлл - Дорога на Уиган-Пирс', 'Стивен Кинг - Оно', 'Буццати Дино - Загадка старого леса',
         'Альбер Камю - Падение', 'Уильям Голдинг - Повелитель мух', 'Чак Паланик - Призраки', 'Жан-Поль Сартр - Тошнота', 'Братья Стругацкие - Понедельник начинается в субботу',
         'Борис Пастернак - Доктор Живаго', 'Джек Лондон - Мартин Иден', 'Теодор Драйзер - Финансист', 'Харпер Ли - Убить пересмешника', 'Эрих Мария Ремарк - Тени в раю',
         'Джордж Оруэлл - Дочь священника', 'Александр Пушкин - Повести Белкина (все произведения)', 'Александр Пушкин - Дубровский', 'Иван Тургенев - Рудин',
         'Денис Фонвизин - Бригадир', 'Пауло Коэльо - Алхимик', 'Александр Пушкин - Арап Петра Великого']

@bot.message_handler(func=lambda message: '1984' in message.text)
def handle_orwell(message):
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Краткое содержание - 1984.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Краткое содержание 1984.txt'
    text = open(file_txt, 'rb')
    bot.send_message(message.chat.id, f'Ожидайте аудиофайл и текст для выбора..')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)


@bot.message_handler(func=lambda message: 'бойцовский клуб' in message.text.lower())
def Club(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Бойцовский Клуб.txt'
    text = open(file_txt, 'rb')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Весь _Бойцовский клуб_ за 10 минут. Краткий пересказ сюжета фильма _Бойцовский клуб_.mp3'
    audio = open(file_path, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'белый клык' in message.text.lower())
def WhiteKl(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Белый клык Кр сод.m4a'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Белый клык.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)


@bot.message_handler(func=lambda message: 'великий гэтсби' in message.text.lower())
def Gatsbi(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Краткое_содержание_Великий_Гэтсби.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Великий Гэтсби.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'на западном фронте без перемен' in message.text.lower())
def Zapad(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/kratkoe-soderzanie-na-zapadnom-fronte-bez-p_Vzy0Uj51.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/На заподном фронте без перемен .txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'недоросль' in message.text.lower())
def Nedorosl(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Краткое содержание - Недоросль.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Недоросль.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'капитанская дочка' in message.text.lower())
def daughter(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Капитанская дочка Пересказ.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Капитанская дочка.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'пиковая дама' in message.text.lower())
def pik(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Пиковая дама.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/пиковая дама.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'человек-амфибия' in message.text.lower())
def person(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Человек-амфибия Краткое содержание.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Человек-амфибия.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'первая любовь' in message.text.lower())
def whitenigths(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Первая любовь.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/первая любовь.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'белые ночи' in message.text.lower())
def WhiteNight(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Белые ночи.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/белые ночи.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'повесть о настоящем человеке' in message.text.lower())
def WhiteNight(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Повесть о настоящем человеке.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, 'Изввините,аудио на это произведение нет в базе..')

@bot.message_handler(func=lambda message: 'путешествия гулливера' in message.text.lower())
def gull(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/путешествие гулливера.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, 'Изввините,аудио на это произведение нет в базе..')

@bot.message_handler(func=lambda message: 'машина времени' in message.text.lower())
def TimeMachine(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/машина времени.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, 'Изввините,аудио на это произведение нет в базе..')

@bot.message_handler(func=lambda message: 'человек-невидимка' in message.text.lower())
def person(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/человек-невидика.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, 'Изввините,аудио на это произведение нет в базе..')

@bot.message_handler(func=lambda message: 'мцыри' in message.text.lower())
def mz(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Краткое содержание - Мцыри.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/мцыри.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'шинель' in message.text.lower())
def mz(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Краткое содержание - Шинель.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/шинель Гоголь.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'ревизор' in message.text.lower())
def revizor(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Краткое содержание - Ревизор.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Гоголь ревизор.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'ася' in message.text.lower())
def asya(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Ася краткое содержание.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/тургенев ася.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'судьба человека' in message.text.lower())
def dream(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/судьба человека краткое содержание.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/судьба человека Шолохов.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'отрочество' in message.text.lower())
def teen(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/отрочество краткое содержание.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/отрочество.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'собачье сердце' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/Собачье сердце краткое сод.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/собачье сердце.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'а зори здесь тихие' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/а зори здесь тихие.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, 'Изввините,аудио на это произведение нет в базе..')

@bot.message_handler(func=lambda message: 'ромео и джульетта' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/ромео и джульетта.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/ромео и джульетта.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'матренин двор' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/матренин двор.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/матренин двор.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'мещанин во дворянстве' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/мещанин аудио.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/мещанин во дворянстве.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'три товарища' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/три товарища краткое сод.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/три товарища ремарк.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'на обратном пути' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/на обратном пути.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")



@bot.message_handler(func=lambda message: 'колыбельная' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Колыбельная Паланик.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'дорога на уиган-пирс' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Дорога на Уиган-Пирс Оруэлл.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'оно' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/оно стивен кинг.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'загадка старого леса' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Загадка старого леса.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'падение' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/падение.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'повелитель мух' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/повелитель мух.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'призраки' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/призраки.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'тошнота' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/тошнота.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'понедельник начинается в субботу' in message.text.lower())
def friends(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/понедельник начинается в субботу.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'доктор живаго' in message.text.lower())
def teen(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/доктор живаго кр сод.mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/доктор живаго краткое сод.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'мартин иден' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/мартин иден.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'финансист' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/финансист.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'убить пересмешника' in message.text.lower())
def teen(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_path = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/убить пересмешника .mp3'
    audio = open(file_path, 'rb')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/убить пересмешника.txt'
    text = open(file_txt, 'rb')
    bot.send_audio(message.chat.id, audio)
    bot.send_document(message.chat.id, text)

@bot.message_handler(func=lambda message: 'тени в раю' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/тени в раю.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'дочь священника' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/Дочь священника.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'повести белкина' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/повести белкина.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'дубровский' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/дубровский.txt'
    text = open(file_txt, 'rb')
    music_file = 'C:/Users/ivann/PycharmProjects/BookBot/Аудио/дубровский.mp3'
    m_file = open(music_file, 'rb')
    bot.send_audio(message.chat.id, m_file)
    bot.send_document(message.chat.id, text)


@bot.message_handler(func=lambda message: 'рудин' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/рудин.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'арап петра великого' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/арап петра великого.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'бригадир' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/бригадир.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: 'алхимик' in message.text.lower())
def dog(message):
    bot.send_message(message.chat.id, 'Ожидайте аудиофайл и текст для выбора..')
    file_txt = 'C:/Users/ivann/PycharmProjects/BookBot/Текста/алхимик.txt'
    text = open(file_txt, 'rb')
    bot.send_document(message.chat.id, text)
    bot.send_message(message.chat.id, "Извините,аудио на это произведение нет в базе..")

@bot.message_handler(func=lambda message: True)
def handletext(message):
    userinput = message.text.strip()
    if not userinput in texts:
        bot.send_message(message.chat.id, "Произведение не найдено,может вы ошиблись в правописание? Попробуйте еще раз.")

@bot.message_handler(content_types=['photo', 'document', 'audio', 'video'])
def get_photo(message):
    bot.send_message(message.chat.id,'Извините,я не могу работать с вашими файлами.Пожалуйста, выберите произведение (/import)')

bot.polling(none_stop=True)
