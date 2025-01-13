# Grade 1. Этап 1. Задание 5

username = input("Имя пользователя: ")
content = input("Описание заметки : ")
status = input("Статус заметки: ")
created_date = input("Дата создания заметки (дд-мм-гггг) : ")
issue_date = input("Дата истечения заметки (дд-мм-гггг) : ")
title1 = input("Заголовок заметки1: ")
title2 = input("Заголовок заметки2: ")

note = [
        username, content, status, created_date, issue_date,
        [title1, title2]
]

print(note)
