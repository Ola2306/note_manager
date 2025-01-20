# Grade 1. Этап 2. Задание 2.
# Работа с циклами и условиями
# Изменение статуса заметки на основе ввода пользователя 
# (возможен ввод как номера статуса, так и наименование статуса)

# Функция ввода номера заметки
def vvod(ii):
    # Ввод номера статуса
    print("Введите информацию о текушем статусе заметки, \n выбрав номер статуса (целое число от 1 до ", len(statuses), ") или набрав его наименование: ")
    print("Выберите номер статуса заметки или наберите наименование статуса заметки: ")
    print("Статус №1: ", statuses[1])
    print("Статус №2: ", statuses[2])
    print("Статус №3: ", statuses[3])
    print("Статус №4: ", statuses[4])
    # Ввод пользователем номера статуса заметки: i - номер статуса заметки
    ii = input("Установить заметке Статус ")
    return ii

# Функция проверки корректности номера заметки
def korr_stat(ii):
    # проверяем является ли введенное значение целой цифрой (да - dd - True, нет - dd - False)
    dd = ii.isdigit()
    # проверяем  корректность введенного номера статуса. В случае некорректности ввода - запрос на повторный ввод номера статуса
    while dd == False:
            print("Введено не корректное значение номера статуса заметки: ", ii, ". Должно вводиться целое число от 1 до ", len(statuses))
            ii = input("Введите номер статуса заметки: ")
            dd = ii.isdigit()
            if dd == True and int(ii) >= 1 and int(ii) <= len(statuses):
                ii = int(ii)
            else: dd = False
            continue
    # вывод установленного пользователем статуса заметки
    return ii

# Функция прверки действительности статуса заметки
def izm_status (new):
    izm = ''
    new = 1
    # Проверка - менялся ли статус заметки по сревнению с введенным ранее
    print("Если статус изменился - введите: 'да('д) или 'yes'(y). \n Если статус заметки не менялся - введите: 'нет'(н) или 'no' (n): ")
    izm = input("Статус заметки изменился? ")
    while not (izm in iizm):
        print("Введено не корректное значение. Возможен один из перечисленных ответов на вопрос: ", iizm)
        print("Заметка имеет статус '", status, "'. \nЕсли статус изменился - введите: 'да'(д) или 'yes' (y).")
        print("Если статус заметки не менялся - введите: 'нет'(н) или 'no'(n): ")
        izm = input("Статус заметки изменился? ")
        continue
    if izm in iizm[::2]:
        print("Статус заметки мзменился. Введите новое значение статуса заметки.")
        new = 1
    else:
        print("Статус заметки действующий")
        new = 2
    return new

# Установим стандартные статусы заметки (создадим словарь Статусов заметок - statuses)
statuses = {
    1: "Получена",
    2: "В работе",
    3: "Отложена",
    4: "Выполнена",
}
# iizm - список возможных ответов на вопрос об изменении статуча; izm - ответ  на вопрос;
# new - 'флаг' надо ли вводить данные о статусе (1 - да, 2 - нет)
ii=''
new = 1
spis = []
iizm = ['yes', 'no', 'y', 'n', 'да', 'нет', 'д', 'н']
izm = ''
while new == 1:
    i = vvod (ii)
    spis = list(statuses.values())
    # Проверка не ввел ли пользователь значение статуса вместо его номера
    if i in spis:
        status = i
    else:
        i1 = korr_stat (i)
        i = int(i1)
        status = statuses[i]
    print("Вы установили статус заметки:", status)
    new = izm_status(new)
    continue
print("Действительный статус заметки:", status)
