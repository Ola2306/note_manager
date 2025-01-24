# Grade 1. Этап 2: Задание 4
# Работа с несколькими заметками

# Ввод даты окончания заметки и проверка корректности введенной даты (соответствия её требуемому формату "ДД-ММ-ГГГГ")
def vvod_date(date_tmp, text1):
    from datetime import datetime
    while True:
        try:
            tnp_date = datetime.strptime(input(f'Введите дату {text1} заметки (дд-мм-гггг): '),'%d-%m-%Y')
        except ValueError:
            print('Введено неверное значение даты. Дата должна быть в формате (дд-мм-гггг)/')
        else:
            date_tmp = tnp_date.strftime("%d-%m-%Y")
            break
    return date_tmp

# Функция ввода и хранения списка словарей  (заметок)
def spis_note(note1, new):
    print(f'Вы моэжете добавить новую заметку. Заметка № {new}:')
    username = input('Имя пользователя: ')
    content = input('Описание заметки: ')
    status = input('Статус заметки: ')
    text1 = 'создания'
    created_date = vvod_date(date_tmp,text1)
    text1 = 'истечения'
    issue_date = vvod_date(date_tmp,text1)
    title = input('Заголовок заметки: ')
    # заполнение списка внесением введенных данных
    note1 = {
        'ID':new,
        'Пользователь': username,
        'Описание заметки': content,
        'Статус': status,
        'Дата создания ': created_date,
        'Дата создания заметки': created_date,
        'Дата истечения заметки': issue_date,
        'Заголовок': title
    }
    return note1

text = ''
date_tmp = ''
tmp_date = ''
note = note1 = []
iizm = ['yes', 'no', 'y', 'n', 'да', 'нет', 'д', 'н']
izm = ''
new = 1
print('Добро пожаловать в "Менеджер заметок"!')
# Ввод нескольких заметок
while True:
    note1 = spis_note(note1, new)
    note.append(note1)
    izm = input(f'Хотите добавить ещё одну заметку? Если да - введите: "да"(д) или "yes" (y).\n Если нет - введите:"нет"(н) или "no"(n) или оставьте поле пустым (нажмите Enter): ')
    if izm in iizm[::2]:
        new += 1
    else:
        break

# вывод информации из списка словарей на экран
print('\nВнесены следующие сведения о заметках:')
for i in range(len(note)):
    print(f'Заметка № {note[i]['ID']} : ')
    print(f'Пользователь: {note[i]['Пользователь']} ')
    print(f'Описание заметки: {note[i]['Описание заметки']} ')
    print(f'Статус заметки: {note[i]['Статус']} ')
    print(f'Дата создания заметки (дд-мм-гггг): {note[i]['Дата создания заметки']} ')
    print(f'Заметка актуальна до (дд-мм-гггг): {note[i]['Дата истечения заметки']} ')
    print(f'Заголовок заметки : {note[i]['Заголовок']} ')

