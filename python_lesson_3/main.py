# Функция с неограниченым количеством аргументов
'''
def sum_numb(*numbers):
    summa = 0
    for i in numbers:
        summa+=i
    return summa

print(sum_numb(1,2,3,4))
'''

# Рекурсия, числа фибоначи
'''
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)

list_1 = []

for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)
'''

# Cортировка слиянием
'''
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
'''