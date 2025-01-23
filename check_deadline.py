# Grade 1. Этап 2. Задание 3.
# Обработка дедлайнов
# Проверка истечения даты окончания и формата даты

# Переменные: today = текущая дата (формат: datetime.datetime), tmp_today - текущая дата в формате дд-мм-гггг,
# issue_date - дата истечения события/заметки (формат: datetime.datetime), issue_date2- дата истечения события/заметки в формате дд-мм-гггг,
# period - период до окончания

period = ''
issue_date = ''
# нахождение текушей даты
from datetime import datetime
today = datetime.today()
tmp_today = today.strftime('%d-%m-%Y')
print('Текущая дата: ', tmp_today)

# Ввод даты окончания заметки и проверка корректности введенной даты (соответствия её требуемому формату "ДД-ММ-ГГГГ")
while True:
    try:
        issue_date = datetime.strptime(input('Введите дату окончания заметки (дд-мм-гггг): '),'%d-%m-%Y')
    except ValueError:
        print('Введено неверное значение даты. Дата должна быть в формате (дд-мм-гггг)/')
    else:
        issue_date2 = issue_date.strftime("%d-%m-%Y")
        break

# проверка истечения срока завершения события/заметки в настоящее время и информирование пользователя о сроках окончания
if today < issue_date:
    tmp_period = issue_date - today
    period = tmp_period.days+1
    print(f'Сегодня {tmp_today}. До даты окончания заметки осталось: {period} дней. Дата окончания: {issue_date2}.')
elif today.day == issue_date.day and today.month == issue_date.month and today.year == issue_date.year:
    print(f'Сегодня {tmp_today}. Дата окончания заметки сегодня. ')
elif today > issue_date:
    tmp_period = today - issue_date
    period = tmp_period.days
    print(f'Сегодня {tmp_today}. Дата окончания заметки уже прошла. Дедлайн истёк {period} дней назад.')




