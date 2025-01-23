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
    print(f"Введите информацию о заметке № {new}:")
    username = input("Имя пользователя: ")
    content = input("Описание заметки : ")
    status = input("Статус заметки: ")
    text1 = 'создания'
    created_date = vvod_date(date_tmp,text1)
    text1 = 'истечения'
    issue_date = vvod_date(date_tmp,text1)
    title = input("Заголовок заметки: ")
    # заполнение списка внесением введенных данных
    note1 = {
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
print("Введите информацию о заметках:")
end = True
# Ввод нескольких заметок
while end:
    note1 = spis_note(note1, new)
    note.append(note1)
    izm = input(f'Хотите добавить ещё одну заметку? Если да - введите: "да"(д) или "yes" (y).\n Если нет - введите:"нет"(н) или "no"(n) или оставьте поле пустым (нажмите Enter): ')
    if izm in iizm[::2]:
        new += 1
        continue
    else:
        end = False
        break

# вывод информации из списка словарей на экран
print('Внесены следующие сведения о заметках:')
for i in range(len(note)):
    print(f'Заметка № {i+1}: ')
    print(f'{note[i]} ')
