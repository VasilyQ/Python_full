
array = [5 , 123, 6, 545, 1]

min = array[0]
max = array[0]

for i in array:
    if i > max:
        max = i
    elif i < min:
        min = i

print(f"min - {min}, max - {max}")