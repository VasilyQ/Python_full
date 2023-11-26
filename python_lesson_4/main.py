#Вызов функции в функции
"""
def calk1(x, b):
    return x*b

def calk2(x, b):
    return x+b

def math(op, x, y):
    print(op(x, y))

math(calk2, 5, 2)
"""

#лямдо функция
"""
def math(op, x, y):
    print(op(x, y))

calk1 = lambda a,b: a+b
math(calk1, 2, 5)

math(lambda a,b: a+b , 2 ,2)
"""

# №1 создает список четных чисел с их квадратом  
"""
list1 = [1, 2, 3, 5, 8, 15, 23, 38]
list2 = []

for i in list1:
    if i % 2 == 0:
        list2.append((i, i*i))

print(list2)
"""

# №2 создает список четных чисел с их квадратом
# (с помощью лямдо функций)
"""
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

list1 = [1, 2, 3, 5, 8, 15, 23, 38]

res = select(int, list1)
res = where(lambda x: x % 2 == 0, res)
res = list(select(lambda x:(x, x**2), res))
print(res)
"""

# функция -> map <- в действии
# функция map принимает на вход функцию и объект 
# и применяет функцию ко всем значениям объекта
"""
list_1 = [x for x in range(1, 10)]
print(list_1)

list_1 = list(map(lambda x: x+10 , list_1))
print(list_1)
"""

# задача решенна с помощью функции -> map
"""
list1 = '1 2 3 4 5 6 7 8 9'
list_2 = list(map(int, list1.split()))
print(list_2)
"""

# функция -> filter <- 
# она принимает на вход функцию и объект 
# и возвращает все знаение в которых функция выдает значение True
"""
data = [15, 22 ,32, 145, 12565]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
"""

# функция -> zip <- 
# функция zip принимает несколько колекций и создает из них картеж 
# первый картеж из первых значений всех колекций потом вторые значения из всех колекций и тд
# создает такое количество кортежий сколько будет минимальное количество значений из всех коллекций
"""
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 2, 3, 4]
salary = [123, 222, 431]

data = list(zip(users, ids, salary))
print(data)
"""

# функция -> enumerate <-
# функция enumerate принимает на вход списек и создает кортеж из индекса и значения 
"""
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)
"""

# работа с фаилами 
# режим -> a <- 
"""
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()
"""
# режим -> w <- 
"""
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
"""
# еще способ работы с режимом -> w <-
"""
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
"""

# режим -> r <- 
"""
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()    
"""

#_____Модуль os_____

# сменить текущую дерикорию 
"""
import os
os.chdir('C:/Users/79190/PycharmProjects/GB')
"""
# узнать текущую дерикторию
"""
import os
print(os.getcwd())  -->  'C:\Users\79190\PycharmProjects\webproject'
"""
# базовое имя пути
"""
import os
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py'))   -->   'main.py'
"""
# Возвращает нормальный, абсолютный путь фаила 
"""
import os
print(os.path.abspath('main.py'))     -->  'C:/Users/79190/PycharmProjects/webproject/main.py'
"""

#_____Модуль shutil_____
"""
import shutil

shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
файл dst.
● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
должен указывать на директорию, а не на символическую ссылку.
"""





