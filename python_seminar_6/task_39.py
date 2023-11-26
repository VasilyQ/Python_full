
list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
list_2 = set(list_2)

list_3 = []

for i in list_1:
    if i not in list_2:
        list_3.append(i)

print(list_3)