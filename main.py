import telebot
import random
import pytz
from telebot import types
from api import FaAPI
import datetime
from schedule import raspisanie
#todo разделять сообщения с расписанием, добавление пункта с направлениями
bot = telebot.TeleBot('5820580999:AAEl6HI68CTWPhkSCExCZbN_3sJ13UQieTc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🗂Контакты")
    btn2 = types.KeyboardButton("📚Студенческие организации")
    btn3 = types.KeyboardButton("🗓Расписание")
    btn4 = types.KeyboardButton("ℹ️Обзор мест")
    btn5 = types.KeyboardButton("©️Цитатник")
    btn6 = types.KeyboardButton("🛎️Обратная связь")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот-навигатор по Финашке.\nЯ помогу тебе узнать актуальное расписание занятий, найти нужную аудиторию, связаться с руководством и многое другое.\nВыбери интересующий тебя вопрос:".format(
                         message.from_user), reply_markup=markup)

def sch1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp = raspisanie(1, message.text)
    if type(rasp) == dict:
        for i in rasp:
            bot.send_message(message.chat.id, text=i, reply_markup=markup, parse_mode='Markdown')
            for x in rasp[i]:
                bot.send_message(message.chat.id, text=x, reply_markup=markup, parse_mode='Markdown')
    elif type(rasp) == str:
        bot.send_message(message.chat.id, text=rasp, reply_markup=markup, parse_mode='Markdown')
def sch2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp = raspisanie(2, message.text)
    if type(rasp) == dict:
        for i in rasp:
            bot.send_message(message.chat.id, text=i, reply_markup=markup, parse_mode='Markdown')
            for x in rasp[i]:
                bot.send_message(message.chat.id, text=x, reply_markup=markup, parse_mode='Markdown')
    elif type(rasp) == str:
        bot.send_message(message.chat.id, text=rasp, reply_markup=markup, parse_mode='Markdown')
def sch3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp = raspisanie(3, message.text)
    if type(rasp) == dict:
        for i in rasp:
            bot.send_message(message.chat.id, text=i, reply_markup=markup, parse_mode='Markdown')
            for x in rasp[i]:
                bot.send_message(message.chat.id, text=x, reply_markup=markup, parse_mode='Markdown')
    elif type(rasp) == str:
        bot.send_message(message.chat.id, text=rasp, reply_markup=markup, parse_mode='Markdown')
def sch4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp = raspisanie(4, message.text)
    if type(rasp) == dict:
        for i in rasp:
            bot.send_message(message.chat.id, text=i, reply_markup=markup, parse_mode='Markdown')
            for x in rasp[i]:
                bot.send_message(message.chat.id, text=x, reply_markup=markup, parse_mode='Markdown')
    elif type(rasp) == str:
        bot.send_message(message.chat.id, text=rasp, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Контакты") or (message.text == "🗂Контакты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Руководство")
        btn2 = types.KeyboardButton("Деканат")
        btn3 = types.KeyboardButton("Медицинский пункт")
        back = types.KeyboardButton("🔙Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери интересующий пункт", reply_markup=markup)
    elif (message.text == "🛎️Обратная связь"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👨‍💻Связаться с создателем")
        back = types.KeyboardButton("🔙Вернуться в главное меню")
        markup.add(btn1, back)
        bot.send_message(message.chat.id, text="Нам было бы очень приятно услышать отзывы и пожелания от вас!\nОставьте свой отзыв в этой гугл [форме](https://forms.gle/hr38R29YGGKxC41x9)", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id, text='😇', reply_markup=markup)
    elif (message.text == "👨‍💻Связаться с создателем"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,text="Всем привет я сделал этого бота используя api от [GeorgiyDemo](https://github.com/GeorgiyDemo) и [Daniil_Utkin](https://github.com/erlnby), также мне помогали собрать общую информацию ребята из группы НАУ22-3.\nЕсли у вас есть какие-то предложения или же вы хотите написать отзыв лично мне в лс, то я был бы очень рад вас услышать!😇😇😇\n\nМой [тг](https://t.me/sulfat_mgso4)",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        back = types.KeyboardButton("🔙Вернуться в главное меню")
        markup.add(back)
    elif (message.text == "Руководство"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="*Засько Вадим Николаевич*\n*Декан факультета*\n_Телефон: (499) 503-47-65_\n_E-mail: VNZasko@fa.ru_", reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id, text="*Курочкин Вадим Васильевич*\n*Советник декана*\n_Телефон: (495) 249-53-48_\n_E-mail: VKyrochkin@fa.ru_\n_Кабинет 514_", reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Клепикова Людмила Васильевна*\n*Первый заместитель декана факультета*\n_Телефон: (495) 249-53-40_\n_E-mail: lvklepikova@fa.ru_\n_Кабинет 514_",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Деканат"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Борисов Олег Игоревич*\n*Заместитель декана по учебной и воспитательной работе*\n_Телефон: (499) 503-47-97_\n_E-mail: oborisov@fa.ru_\n[Vk](https://vk.com/borisov.oleg)\n_Кабинет 219_",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id,
                         text="*Курбаналиева Лала Фаризовна*\n*Менеджер, помощник декана*\n_Телефон: (499)503-47-65_\n_E-mail: lfkurbanalieva@fa.ru_\n[Vk](https://vk.com/id146079203)\n_Кабинет 221_",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id,
                         text="*Васильченко Анна Дмитриевна*\n*Менеджер*\n_Телефон: (495)249-53-41 (доб. 3)_\n_E-mail: AnDVasilchenko@fa.ru_\n[Vk](https://vk.com/vasilchenkoanna)\n_Кабинет 208_",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        bot.send_message(message.chat.id,
                         text="*Осипова Виктория Геннадьевна*\n*Специалист по Учебно-методической работе 1 категории (бакалавриат)*\n_Телефон: (495)249-53-41 (доб. 1-3)_\n_E-mail: vosipova@fa.ru_\n[Vk](https://vk.com/sonya_irbis)\n_Кабинет 202_",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
    elif (message.text == "Медицинский пункт"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Назаренко Светлана Михайловна*\n*Главный специалист*\n_Телефон: (495)249-53-41 (доб. 1-1)_\n_E-mail: taxdep@fa.ru_\n_Кабинет 202_",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "🔙Вернуться в главное меню") or (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🗂Контакты")
        btn2 = types.KeyboardButton("📚Студенческие организации")
        btn3 = types.KeyboardButton("🗓Расписание")
        btn4 = types.KeyboardButton("ℹ️Обзор мест")
        btn5 = types.KeyboardButton("©️Цитатник")
        btn6 = types.KeyboardButton("🛎️Обратная связь")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id,
                         text="Вы вернулись в главное меню.".format(message.from_user), reply_markup=markup)
    elif (message.text == "Студенческие организации") or (message.text == '📚Студенческие организации'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Студии")
        btn2 = types.KeyboardButton("Организации")
        btn3 = types.KeyboardButton("Спортивные сборные")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери интересующий пункт", reply_markup=markup)
    elif (message.text == "Студии"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Хореографическая студия «Frappe».\n\nВо «Frappe» танцуют только девушки, а упор делается на классические танцы. Репертуар включает эстрадную и стилизованную хореографию. Участницы выступают на фестивалях искусства по всему миру.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Студия современного танца «Liberté».\n\nХореографическая студия объединяет студентов, которые проявляют себя в разных направлениях: контемпорари, джаз-фанк, леди дэнс, хип-хоп и вог. Члены коллектива часто выступают на крупнейших сценах нашей страны, в том числе с известными музыкантами.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Хор Финансового университета.\n\nУчастники хора исполняют произведения разных стилей: от классики до современных популярных песен. Выступления проходят и на крупных площадках города, и на полноценных концертах.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Вокальный ансамбль «FINMUSE».\n\nЗдесь каждому желающему не просто поставят голос, а научат держаться ярко и уверенно на сцене*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Ансамбль барабанщиков.\n\nАнсамбль барабанщиков создан для тех, кто хочет научиться или уже умеет отбивать ритм. В этом творческом коллективе готовят яркие шоу-номера для торжественных мероприятий и маршевые композиции.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Ансамбль народной песни.\n\nВ ансамбле народной песни вокалисты исполняют песни в стиле русского народного творчества, фольклора, патриотического характера и лирического настроя.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Студия Фортепианной музыки*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Вокально-инструментальный ансамбль «Атмосфера».\n\nВокально-инструментальная группа, которая объединяет все стили музыки и представляет Финансовый Университет на лучших конкурсах столицы и международных фестивалях. Тебя ждут яркие репетиции, выступления и запись любимых треков в музыкальной студии!*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Студенческий театр «ФуНТ».\n\nВ театре ставят комедии, пьесы и серьёзные постановки. Актёры работают над своей подачей, манерой разговора, дикцией, мимикой и артистическими способностями.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Студия ведущих.\n\nСтудия ждёт ребят, которые имеют опыт ведения мероприятий, обладают ораторским искусством и актёрским мастерством. Здесь учат вести мероприятия, заводить публику, выстраивая с нуля дикцию, навык публичного выступления и голос.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Организации"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Студенческий совет.\n\nСтуденческий совет — организация студенческого самоуправления, которая представляет права, помогает решать проблемы студентов, а также организует внеаудиторную жизнь через проведение проектов.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Информационный комитет.\n\nИнформационный комитет — подразделение Студенческого совета Финансового университета, организующий информационную поддержку мероприятий и событий университета по направлениям: СМИ, фото, видео, дизайн, цифровые технологии.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Проектный комитет.\n\nПроектный комитет – одна из составляющих Студенческого совета, которая ежегодно проводит множество спортивных и культурно-массовых мероприятий, создавая пространство для развития творческого вкуса студентов.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Комитет внешних связей.\n\nКомитет внешних связей – подразделение Студенческого совета Финансового университета, которое сотрудничает с компаниями на тему трудоустройства, организации экскурсий, оказание спонсорской поддержки мероприятиям ССт.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Учебный комитет.\n\nУчебный комитет разбирает все трудные моменты в учёбе и готов подсказать ответ на вопрос. Перед сессией организуют курсы подготовки к экзаменам.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Социальный комитет.\n\nСоциальный комитет — подразделение Студенческого совета Финансового университета при Правительстве РФ, который оказывает социальную помощь студентам при решении их проблем и осуществляет благотворительную деятельность и продвигаем осознанность и защиту окружающей среды.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Объединенный комитет общежитий.\n\nОбъединенный комитет общежитий занимается проблемами студентов, проживающих в общежитиях, консультирует их по всем вопросам, связанными с заселением.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Тренинг-центр.\n\nТренинг-Центр обучает и следит за развитием Студенческого совета, проводит мероприятия по улучшению навыков активистов, занимаются их адаптацией в организации*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Научное Студенческое Общество.\n\nОрганизуют крупнейшие научные мероприятия: МНСК, ВузЭкоФест, информационная поддержка научных проектов.*",
                         reply_markup=markup, parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         text="*Волонтерский центр.\n\nВолонтёрская поддержка на мероприятиях Финансового университета любого масштаба вплоть до крупнейших международных форумов.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Спортивные сборные"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,text="*Адаптивный спорт\nАлтимат-фрисби\nАрмреслинг\nБадминтон\nБаскетбол (мужская сборная)\nБаскетбол (женская сборная)\nБиатлон\nБоевое самбо\nБокс\nВодное поло\nВолейбол (женская сборная)\nВолейбол (мужская сборная)\nВольная борьба\nГандбол (мужская сборная)\nГандбол (женская сборная)\nГиревой спорт\nГонка ГТО\nГорнолыжный спорт\nГреко-римская борьба\nДартс\nДзюдо\nКапоэйра\nКаратэ\nКерлинг\nЛегкая атлетика\nЛыжные гонки\nМини-футбол (женская сборная)\nМини-футбол (мужская сборная)\nMMA\nНастольный теннис (женская сборная)\nНастольный теннис (мужская сборная)\nПарусный спорт\nПауэрлифтинг и жим лёжа\nПейнтбол\nПеретягивание каната\nПлавание\nПляжный волейбол (мужская сборная)\nПляжный волейбол (женская сборная)\nПляжный футбол (мужская сборная)\nПляжный футбол (женская сборная)\nПолиатлон\nПулевая стрельба\nРегби\nРитмическая гимнастика\nСамбо\nСпортивная аэробика\nСпортивная гимнастика\nСпортивное ориентирование\nТанцевальный спорт\nТеннис\nТуризм\nТяжелая атлетика\nФехтование\nФитнес-аэробика\nФутбол (мужская сборная)\nФутбол (женская сборная)\nХоккей\nХудожественная гимнастика\nЧир-спорт\nШахматы\nШашки\nЭстетическая гимнастика*",
                        reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Расписание") or (message.text == '🗓Расписание'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Расписание на сегодня")
        btn2 = types.KeyboardButton("Расписание на завтра")
        btn3 = types.KeyboardButton("Расписание на эту неделю")
        btn4 = types.KeyboardButton("Расписание на следующую неделю")
        back = types.KeyboardButton("🔙Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Выбери интересующий пункт", reply_markup=markup)
    elif (message.text == 'Расписание на сегодня'):
        msg = bot.send_message(message.from_user.id, 'Введите номер вашей группы (Например: НАУ22-3).')
        bot.register_next_step_handler(msg, sch1)
    elif (message.text == 'Расписание на завтра'):
        msg = bot.send_message(message.from_user.id, 'Введите номер вашей группы (Например: НАУ22-3).')
        bot.register_next_step_handler(msg, sch2)
    elif (message.text == 'Расписание на эту неделю'):
        msg = bot.send_message(message.from_user.id, 'Введите номер вашей группы (Например: НАУ22-3).')
        bot.register_next_step_handler(msg, sch3)
    elif (message.text == 'Расписание на следующую неделю'):
        msg = bot.send_message(message.from_user.id, 'Введите номер вашей группы (Например: НАУ22-3).')
        bot.register_next_step_handler(msg, sch4)

    elif (message.text == "Обзор мест") or (message.text == 'ℹ️Обзор мест'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Столовая")
        btn2 = types.KeyboardButton("Библиотека")
        btn3 = types.KeyboardButton("Автоматы с едой")
        btn4 = types.KeyboardButton("Коворкинг")
        back = types.KeyboardButton("🔙Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Выбери интересующий пункт", reply_markup=markup)
    elif (message.text == "Столовая"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Локация: 4 подъезд , -1 этаж.*\n\n_Режим работы: пн-пт 9:00-18:00_\n\n*Меню и цены:\nСалат Витаминный - 60\nСалат свекла с майонезом - 60\nСалат Карибский - 85\nСалат Капрезе - 90\nСалат Ветчина с грибами - 95\nСалат Фруктовый - 100\nСалат Цезарь с курицей - 150\nСуп Рассольник с курицей - 85\nСуп Лапша Грибная - 90\nКрем суп Брокколи - 100\nПлов Вермишелевый с курицей - 165\nКуриное филе отварное - 150\nШницель свиной рубленый - 150\nПаст Карбонара - 175\nИндейка в панировке 185\nКуриное филе СС соленым огурцом - 185\nФиле рыбы жареное в яйце - 185\nСвинина по-итальянски - 195\nБефстроганов - 215\nМакароны - 40\nРис - 50\nГречка - 60\nКартофель отварной - 70\nОвощи на пару - 90\nЧай с сахаром - 30\nКомпот из сухофруктов - 30\nКомпот из ягод - 35*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Библиотека"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Все библиотечные помещения находятся на первом этаже компьютерного корпуса:\nКабинет 102-1 - библиотека, фонд старших курсов, читальный зал\nКабинет 103-1 - библиотека, фонд младших курсов\nКабинет 101-1 - медиатека\nТакже между кабинетами 102-1 и 103-1 находится стенд с книгами, которые может взять любой желающий*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Автоматы с едой"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 этаж")
        btn2 = types.KeyboardButton("2 этаж")
        btn3 = types.KeyboardButton("3 этаж")
        btn4 = types.KeyboardButton("4 этаж")
        btn5 = types.KeyboardButton("5 этаж")
        back = types.KeyboardButton("🔙Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выбери интересующий пункт", reply_markup=markup)
    elif (message.text == "5 этаж"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*6 подъезд (у кабинета 557)\n\n🔘Автомат с едой «ВкусВилл»\nВода ≈ 70-90 руб.\nСоки/газировки ≈ 70-100руб.\nРоллы/сэндвичи ≈ 140-265руб.\nБатончики/козинаки/чак-чак/вафли/пряники и др ≈ 50-110руб.\nШоколад ≈ 210руб.\nСушки/печенье ≈ 90-125руб.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "4 этаж"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*4 подъезд (у кабинета 433)\n\n🔘Бариста\nКофе/горячий шоколад/какао и др. ≈ 100-260руб.\nВода = 50руб.\nВозможно использование альтернативного молока и сиропов Пончики = 110руб.\nОнигири = 170руб.\nПита ≈ 200-220руб.\nСэндвичи ≈ 160-190руб.\nПеченье = 110руб.\nМини-пицца = 110руб.*\n\n*6 подъезд (у кабинета 455):\n\n🔘Автомат с едой «ВкусВилл»\nБатончики/козинаки/чак-чак/вафли/пряники и др. ≈ 50-110руб.\nВода ≈ 70-90 руб.\nСоки/газировки ≈ 70-100руб.\nРоллы/сэндвичи ≈ 140-265руб\nСушки/печенье ≈ 90-125руб.\n\n🔘Кофемашина «Шоколадница»\nКофе ≈ 100-175руб.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "3 этаж"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*5 подъезд (у кабинета 349)\n\n🔘Автомат с едой «Snakky»\nВода = 60руб.\nЧай/газировка ≈ 80-95руб.\nБатончики шоколадные ≈ 55-65руб.\nОрешки/чипсы ≈ 50-60руб.\nВафли = 70руб.\n\n🔘Кофемашина\nКофе ≈ 40-60руб.\n6 подъезд (у кабинета 357) Автомат с едой «Snakky»\nВода = 60руб.\nЧай/газировка ≈ 80-95руб. Батончики шоколадные ≈ 55-65руб. Орешки/чипсы ≈ 50-60руб.\nВафли = 70руб.\n\n🔘Кофемашина\nКофе ≈ 70-100руб.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "2 этаж"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*4 подъезд (у кабинета 234)\n\n🔘Бариста\nКофе/горячий шоколад/какао и др. ≈ 100-260руб.\nВода = 50руб.\nВозможно использование альтернативного молока и сиропов Пончики = 110руб.\nОнигири = 170руб.\nПита ≈ 200-220руб.\nСэндвичи ≈ 160-190руб.\nПеченье = 110руб.\nМини-пицца = 110руб.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "1 этаж"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*5 подъезд (у кабинета 149 и 145)\n\n🔘Автомат с едой «ВкусВилл»\nВода ≈ 70-90 руб.\nСоки/газировки ≈ 70-100руб.\nРоллы/сэндвичи ≈ 140-265руб.\nБатончики/козинаки/чак-чак/вафли/пряники и др. ≈ 50-110руб.\nШоколад ≈ 210руб.\nСушки/печенье ≈ 90-125руб.\n\n🔘Автомат с кофе «Азбука вкуса»\nКофе ≈ 150-200руб.*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Коворкинг"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("4 подъезд")
        btn2 = types.KeyboardButton("5 подъезд")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбери интересующий пункт", reply_markup=markup)
    elif (message.text == "4 подъезд"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*1 этаж - около аудитории 129\n\n3 этаж - около аудитории 333*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "5 подъезд"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*4 этаж - около аудитории 447\n\n5 этаж - около аудитории 547*",
                         reply_markup=markup, parse_mode='Markdown')
    elif (message.text == "Цитатник") or (message.text == '©️Цитатник'):
        f = open('citati.txt').read()
        c = f.replace('#','©').replace('_',' ').split('\n\n')
        r = random.randint(0,62)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,text=c[r],reply_markup=markup, parse_mode='Markdown')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="*Выберите интересующий пункт.*",
                         reply_markup=markup, parse_mode='Markdown')

bot.polling(none_stop=True)
