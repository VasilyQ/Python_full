# с помощью лямбда функций опрдеделить является ли число 2-х значным

n = 1

f = lambda x: x // 100
res = f(abs(n))

if res <= 0:
    print('yes')
else:
    print('no')


# def show_menu():
#     print('1. Распечатать справочник'
#           '2. Найти телефон по фамилии'
#           '3. Изменить номер телефона'
#           '4. Удалить запись'
#           '5. Найти абонента по номеру телефона'
#           '6. Добавить абонента в справочник'
#           '7. Закончить работу', sep = '\n')
#     choice=int(input())
#     return choice