# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

# n = 'пара-ра-рэм рам-пам-папам па-ра-по-даа'
# list_1 = n.split()
# q = set()
# count = 0


def countNumber(new_list):
    count=0
    for i in new_list:
        if i in 'уеыаоэяию':
            count+=1
    return count


n = 'пара-ра-рэмя рам-пам-папам-па ра-по-даэя'
list_1 = n.split()
if len(list_1) <=1:
    print('Количество фраз должно быть больше одной!')
else:
    res = set(map(lambda x: countNumber(x), list_1))
    if len(res) <=1:
        print('Парам пам-пам')
    else:
        print('Пам парам')