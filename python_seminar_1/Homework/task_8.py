# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

a = 4
b = 1
c = 3

if c%a == 0 or c%b == 0:
    print('yes')
else:
    print('no')
    print(c/a , c/b)