from api import FaAPI
import pytz
import datetime
def raspisanie(mode, gr):
    fa = FaAPI()
    group = fa.search_group(gr)
    schedule = {}
    data = ''
    aud = ''
    name_lesson = ''
    adr = ''
    kind_of_work = ''
    time_start = ''
    time_end = ''
    teacher = ''
    if mode == 1:
        tz = pytz.timezone('Europe/Moscow')
        tt = (str(datetime.datetime.now(tz))).split(' ')
        date = tt[0].replace('-', '.')
        date1 = date
        date2 = date
    elif mode == 2:
        tz = pytz.timezone('Europe/Moscow')
        day = int((datetime.datetime.now(tz)).strftime('%w'))
        tt = datetime.datetime.now(tz)
        date1 = (((str(tt + datetime.timedelta(1))).split(' '))[0]).replace('-', '.')
        date2 = date1
    elif mode == 3:
        tz = pytz.timezone('Europe/Moscow')
        day = int((datetime.datetime.now(tz)).strftime('%w'))
        tt = datetime.datetime.now(tz)
        if day >= 1 and day <= 6:
            razn1 = day - 1
            razn2 = 6 - day
            date1 = (((str(tt - datetime.timedelta(razn1))).split(' '))[0]).replace('-','.')
            date2 = (((str(tt + datetime.timedelta(razn2))).split(' '))[0]).replace('-','.')
        elif day == 0:
            date1 = (((str(tt - datetime.timedelta(6))).split(' '))[0]).replace('-','.')
            date2 = (((str(tt - datetime.timedelta(1))).split(' '))[0]).replace('-','.')
    elif mode == 4:
        tz = pytz.timezone('Europe/Moscow')
        day = int((datetime.datetime.now(tz)).strftime('%w'))
        tt = datetime.datetime.now(tz)
        if day >= 1 and day <= 6:
            razn1 = 8 - day
            razn2 = 14 - day
            date1 = (((str(tt + datetime.timedelta(razn1))).split(' '))[0]).replace('-', '.')
            date2 = (((str(tt + datetime.timedelta(razn2))).split(' '))[0]).replace('-', '.')
        elif day == 0:
            date1 = (((str(tt + datetime.timedelta(1))).split(' '))[0]).replace('-', '.')
            date2 = (((str(tt + datetime.timedelta(7))).split(' '))[0]).replace('-', '.')

    '''
    mode1 = 1 = schedule for today
    mode2 = 1 = schedule for tomorrow
    mode3 = 6 = schedule for this week
    mode4 = 6 = schedule for next week
    '''
    try:
        timetable = fa.timetable_group(group[0]["id"], date1, date2)
        #print(date1)
        #print(date2)
    except IndexError:
        return 'Такая группа не найдена 😣'
    for i in timetable:
        for x in i:
            if x == 'auditorium':
                aud = i[x]
                if '_' in aud:
                    aud = aud.replace('_', ' ')
            elif x == 'building':
                adr = i[x]
            elif x == 'beginLesson':
                time_start = i[x]
            elif x == 'endLesson':
                time_end = i[x]
            elif x == 'discipline':
                name_lesson = i[x]
            elif x == 'kindOfWork':
                kind_of_work = i[x]
            elif x == 'date':
                temp = i[x].split('.')
                data = temp[2] + '.' + temp[1] + '.' + temp[0]
            elif x == 'lecturer':
                teacher = i[x]
        message = (kind_of_work + ': ' + name_lesson + '\n' + 'Время занятия: ' + time_start + ' - ' + time_end + '\n' + 'Преподаватель: ' + teacher + '\n' + 'Адрес: ' + adr + '\n' + 'Аудитория: ' + aud + '\n')
        if data not in schedule:
            schedule[data]=[message]
        else:
            schedule[data].append(message)
    if len(schedule) > 0:
        return schedule
    else:
        return 'Пары на этот период времени отсутствуют.'

'''
r = raspisanie(2, 'НАУ22-3')
for i in r:
    print(i)
    for x in r[i]:
        print(x)'''
#print(raspisanie(2, 'НАУ22-3'))
