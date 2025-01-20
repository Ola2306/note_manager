# Grade 1. Этап 2. Задание 1
# Работа с циклами и условиями
# Пояснение: titles - список заголовков заметок, i+1 - номер заголовка заметки; end - 'стоп-переменная'

titles = {}
i = 0
print("Введите информацию о заметке:")
end = True
while end:
    title = {i+1: input(f"Введите заголовок {i+1}(или для завершения ввода оставьте поле пустым (нажмите Enter) или наберите стоп): ")}
    i += 1
    titles.update(title)
    tit1 = str(titles[i])
    # проверка на завершение ввода информации (стоп - не зависимо от регистра как в русской, так и в латинской раскладке)
    if titles[i] == "" or tit1.lower() == "стоп" or tit1.lower() == "stop": end = False
# удаление последнего (пустого, стоп) элемента (завершение ввода)
titles.pop(i)
n = i-1

# Вывод на экран результирующей информации, введенной пользователем
print("Внесены следующие сведения о заметке:")
print("кол-во заголовков:", n, "\nЗаголовки:\n", titles)

# Проверка уникальности введенных значений. Удаление дублей заголовков.
# "флажки": n - число заметок в словаре; s - номера одинаковых заголовков; i,j - счетчики цикла; tit1, title - промежуточные переменнные
s = []
i = 1
j = 2
while i < n:
 # проверка валидности i
    while i < n:
        if i in s: i += 1
        else: break
    tit1 = titles[i]
    i += 1
    while i < n:
        if i in s: i += 1
        else: break
    j = i
    while j < n+1:
        while j < n+1:
            if j in s: j += 1
            else:  break
        if j > n: continue
        else:
            title = titles[j]
            if tit1 == title:
                 del titles[j]
                 s.append(j)
            j += 1

print("Вами введены следующие уникальные сведения о заметке:")
print("Кол-во заголовков:", len(titles), "\nЗаголовки:\n", titles)
