# Задача 22: Даны два неупорядоченных набора целых
#  чисел (может быть, с
# повторениями). Выдать без повторений в порядке 
# возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа.
#  n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5'
list_1 = set(var2.split())
list_2 = set(var3.split())

list_3 = sorted(list_1.intersection(list_2))

for i in list_3:
    print(i, end = ' ')

# print(*list_3)

