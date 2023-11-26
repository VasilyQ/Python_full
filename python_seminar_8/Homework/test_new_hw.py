# Меню
def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Сохранить данные',
          '8. Завершить работу', sep = '\n')
    choice=int(input())
    return choice

# Добавить текст в программу
def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'телефон', 'описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            if '\n' in record['описание']:
                record['описание'] = record['описание'][:-1]
            phone_book.append(record)	
    return phone_book


# 1. Распечатать справочник
def print_phb(phone_book):
    list_1 = []
    for i in range(len(phone_book)):
        for(k,v) in phone_book[i].items():
            list_1.append(v)
        print(i," : ".join(list_1))
        list_1 = []

# функция преобразования словаря в строку
def print_dict(dict_1):
    list_1 = []
    for(k,v) in dict_1.items():
        list_1.append(v)
    return " : ".join(list_1)

# 2. Найти телефон по фамилий
def find_by_lastname(phone_book,last_name):
    count = 0
    flag = False
    last_name = last_name.lower()
    for i in phone_book:
        count+=1
        if i['Фамилия'].lower() == last_name:
            print(f'{count-1} {print_dict(i)}')
            flag = True
    if flag == False:
        print('такого абонента нет')

# 3. Изменить номер телефона
def change_number(phone_book,last_name,new_number):
    count = 0
    list_1 = []
    last_name = last_name.lower()
    for i in phone_book:
        count+=1
        if i['Имя'].lower() == last_name or i['Фамилия'].lower() == last_name:
            print(f"{count-1} {print_dict(phone_book[count-1])}")
            list_1.append(count-1)
    if len(list_1) > 1:
        id_phb = None
        while id_phb not in list_1:
            id_phb = int(input('Введите id абонента которому хотите изменить номер: '))
            print('такого id нет')
        phone_book[id_phb]['телефон'] = str(new_number)
    elif len(list_1) == 0:
        print(" такого абонента нет в списке")
    else:
        (phone_book[list_1[0]])['телефон'] = str(new_number)
        print('номер изменен')
    return phone_book

# 4. Удалить запись
def delete_by_lastname(phone_book,lastname):
    list_1 = []
    lastname = lastname.lower()
    count = 0
    for i in phone_book:
        count+=1
        if i['Имя'].lower() == lastname or i['Фамилия'].lower() == lastname:
            print(f"{count-1} {print_dict(phone_book[count-1])}")
            list_1.append(count-1)
    if len(list_1) > 1:
        id_phb =None
        while id_phb not in list_1:
            id_phb = int(input('Введите id абонента которого хотите удалить: '))
            print('такого id нет')
        print('абонент удален!')
        phone_book.pop(id_phb)
    elif len(list_1) == 0:
        print(" такого абонента нет в списке")
    else:
        print('абонент удален!')
        phone_book.pop(list_1[0])

    return phone_book

# 5. Найти абонента по номеру телефона
def find_by_number(phone_book,number):
    count = 0
    flag = False
    for i in phone_book:
        count+=1
        if i['телефон']== number:
            print(f'{count-1} {print_dict(i)}')
            flag = True
    if flag == False:
        print('такого абонента нет')

# 6. Добавить абонента в справочник
def add_user(phone_book):
    fields=['Фамилия', 'Имя', 'телефон', 'описание']
    q = dict()
    for i in fields:
        q[i] = input(f"{i}: ")
    phone_book.append(q)
    print_dict(q)
    return phone_book

# 7. Сохранить данные
def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

# вся цепочка программы
def work_with_phonebook():

    choice=show_menu()
    print()
    phone_book=read_txt('D:\python\python_seminar_8\Homework/phonebook.csv')
    while (choice!=8):
        if choice==1:
            print_phb(phone_book)
            print()
        elif choice==2:
            last_name=input('Введите Фамилию: ')
            find_by_lastname(phone_book,last_name)
            print()
        elif choice==3:
            last_name=input('Введите имя или фамилию: ')
            new_number=input('Введите новый номер телефона: ')
            change_number(phone_book,last_name,new_number)
            print()
        elif choice==4:
            lastname=input('Введите имя или фамилию: ')
            delete_by_lastname(phone_book,lastname)
            print()
        elif choice==5:
            number=input('Введите номер ')
            find_by_number(phone_book,number)
            print()
        elif choice==6:
            add_user(phone_book)
            print()
        elif choice==7:
            (write_txt('D:\python\python_seminar_8\Homework/phonebook.csv' , phone_book))
            print('Изменения внесени в фаил')
            print()
        elif choice < 1 and choice > 8:
            print('функции под этим номером нет')
            print()
              
        choice=show_menu()
        print()


work_with_phonebook()
