# Grade 1. Этап 2: Задание 4
# Работа с несколькими заметками
# Программа позволяет:
# - Вводить список заметок, при этом проверяет:
#       -- соответствие формата вводимых дат
#       -- чтобы заголовок заметки был не пустой
#       -- устанавливать статус заметки в соответствии со списком статусов (и проверяет корректность вводимого статуса)
# - Удалять ошибочно введенную заметку (по желанию пользователя), при этом проверяет:
#       -- корректность номера ID удаляемой заметки
#           (в том числе случай, когда пользователь случайно вводит не цифровое значение)
#       -- не пустой ли список
# Осушествляется вывод на экран результирующего списка заметок:
# после ввода списка и после удаления ошибочных заметок

# Функция проверки корректности номера заметки
def korr_stat(ii):
    # проверяем является ли введенное значение числом (да - dd - True, нет - dd - False)
    dd = ii.isdigit()
    # проверяем  корректность введенного номера/наименования статуса. В случае некорректности ввода - запрос на повторный ввод номера статуса
    while dd == False:
            print(f'Введено не корректное значение номера или наименования статуса заметки: {ii}.\nДолжно вводиться целое число от 1 до {len(statuses)} или наименование статуса из списка.')
            ii = input('Введите номер или наименование статуса заметки: ')
            #dd = ii.isdigit()
            if ii in spis:
                break
            else:
                dd = ii.isdigit()
                if dd == True and int(ii) >= 1 and int(ii) <= len(statuses):
                    ii = int(ii)
                    break
                else:
                    dd = False
            continue
    # вывод установленного пользователем статуса заметки
    return ii

# Функция ввода значения статуса заметки
def inp_status():
    # Ввод номера статуса
    print(f'Введите информацию о текушем статусе заметки, \n выбрав номер статуса (целое число от 1 до {len(statuses)}): ')
    print('Выберите номер статуса заметки: ')
    print(f'Статус №1: {statuses[1]}')
    print(f'Статус №2: {statuses[2]}')
    print(f'Статус №3: {statuses[3]}')
    print(f'Статус №4: {statuses[4]}' )
    # Ввод пользователем номера статуса заметки: ii - номер статуса заметки
    ii = input('Установить заметке Статус ')
    return  ii

# Функция выбора статуса заметки из списка статусов
def stat(ii):
    while True:
        i = inp_status()
        # Проверка не ввел ли пользователь значение статуса вместо его номера
        if i in spis:
            status = i
            break
        else:
            i1 = korr_stat(i)
            if i1 in spis:
                status = i1
                break
            else:
                i = int(i1)
                status = statuses[i]
                break
    return  status

# Ввод нескольких заметок (Менеджер заметок)
def notes_manager(note, note1, new):
    print('Добро пожаловать в "Менеджер заметок"!')
    while True:
        note1 = inp_note(note1, new)
        note.append(note1)
        change = input(f'Хотите добавить ещё одну заметку? Если да - введите: "да"(д) или "yes" (y).\n Если нет - введите:"нет"(н) или "no"(n) или оставьте поле пустым (нажмите Enter): ')
        if change == '':
            break
        else:
            while not (change in change_stat):
                print(f'Введено не корректное значение. Возможен один из перечисленных ответов на вопрос:  {change_stat}')
                change = input(f'Хотите добавить ещё одну заметку? Если да - введите: "да"(д) или "yes" (y).\n Если нет - введите:"нет"(н) или "no"(n) или оставьте поле пустым (нажмите Enter): ')
                if change == '':
                    break
                continue
            if change in change_stat[::2]:
                new += 1
            else:
                break
    return note

# Функция ввода и хранения списка словарей (заметок)
def inp_note(note1, new):
    ii = ''
    print(f'Вы моэжете добавить новую заметку. Заметка № {new}:')
    end = True
    while True:
        title = input(f"Введите заголовок заметки (для завершения ввода оставьте поле пустым (нажмите Enter) или наберите стоп): ")
        if title == "" or title.lower() == "стоп" or title.lower() == "stop":
            end = False
            print(f'Ввод информации о заметке прекращен.')
        break
    if end == True:
        username = input('Имя пользователя: ')
        content = input('Описание заметки: ')
        status = stat(ii)
        text1 = 'создания'
        created_date = inp_date(date_tmp,text1)
        text1 = 'истечения'
        issue_date = inp_date(date_tmp,text1)
        # дополнение списка введенными данными
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

# Функция проверки корректности номера заметки
def edit_note(ii):
    # проверяем  корректность введенного номера заметки. В случае некорректности ввода - запрос на повторный ввод номера заметки
    if int(ii) < 1 or int(ii) > len(note):
        dd = False
    else:
        dd = True
    while dd == False:
        print(f'Введено неверное значение. Номер заметки - целое число от 1 до {len(note)}.')
        while True:
            try:
                ii = int(input(f'Введите номер заметки, которую надо удалить (целое число от 1 до {len(note)}): '))
            except ValueError:
                print(f'Введено неверное значение. Номер заметки целое число от 1 до {len(note)}.')
            else:
                break
        if ii >= 1 and ii <= len(note):
            break
        else:
            continue
    return ii

# Ввод даты начала/окончания заметки и проверка корректности введенной даты (соответствия её требуемому формату "ДД-ММ-ГГГГ")
def inp_date(date_tmp, text1):
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

# вывод информации из списка словарей на экран
def out_note():
    for i in range(len(note)):
        print(f'Заметка № {note[i]['ID']} : ')
        print(f'Пользователь: {note[i]['Пользователь']} ')
        print(f'Описание заметки: {note[i]['Описание заметки']} ')
        print(f'Статус заметки: {note[i]['Статус']} ')
        print(f'Дата создания заметки (дд-мм-гггг): {note[i]['Дата создания заметки']} ')
        print(f'Заметка актуальна до (дд-мм-гггг): {note[i]['Дата истечения заметки']} ')
        print(f'Заголовок заметки : {note[i]['Заголовок']} ')
    return

text = ''
date_tmp = tmp_date = ''
note = note1 = []
change_stat = ['yes', 'no', 'y', 'n', 'да', 'нет', 'д', 'н', 'Yes', 'No', 'Y', 'N', 'Да', 'Нет', 'Д', 'Н', 'YES', 'NO', 'ДА', 'НЕТ']
change = ''
# Установим стандартные статусы заметки (создадим словарь Статусов заметок - statuses)
statuses = {
    1: 'Получена',
    2: 'В работе',
    3: 'Отложена',
    4: 'Выполнена',
}
spis = list(statuses.values())
new = 1
# вызов Менеджера заметок для ввода списка словарей
notes_manager(note, note1, new)
# вывод информации из списка словарей на экран
print('\nВнесены следующие сведения о заметках:')
out_note()

if len(note) == 0:
    print('\nСписок заметок пустой.')
else:
    # удаление информации о заментке из списка словарей
    print('\nПроверьте введенные данные. \nВ случае выявления ошибки - ошибочную заметку можно удалить.')
    while True:
        if len(note) == 0:
            print('\nСписок заметок пустой.')
            break
        change = input(f'Надо удалить некорректную заметку? Если да - введите: "да"(д) или "yes" (y).\n Если нет - введите:"нет"(н) или "no"(n) или оставьте поле пустым (нажмите Enter): ')
        if change == '':
            break
        else:
            while not (change in change_stat):
                print(f'Введено не корректное значение. Возможен один из перечисленных ответов на вопрос:  {change_stat}')
                change = input(f'Надо удалить некорректную заметку? Если да - введите: "да"(д) или "yes" (y).\n Если нет - введите:"нет"(н) или "no"(n) или оставьте поле пустым (нажмите Enter): ')
                if change == '':
                    break
                continue
            if change == '': break
            elif change in change_stat[::2]:
                while True:
                    try:
                        tmp_new = int(input(f'Введите номер заметки, которую надо удалить (целое число от 1 до {len(note)}): '))
                    except ValueError:
                        print(f'Введено неверное значение. Номер заметки - это целое число от 1 до {len(note)}.')
                    else:
                        break
                new = edit_note(tmp_new)
                new = int(new)
                i = 0
                while i < len(note):
                    if note[i]['ID'] == new:
                        del note[i]
                        print(F'Заметка № {new} удалена. В списке осталось: {len(note)} заметок.')
                        break
                    else:
                        i += 1
                        continue
            else:
                break
        continue

    # вывод итоговой информации из списка словарей на экран
    print('\nОстались следующие сведения о заметках:')
    out_note()
