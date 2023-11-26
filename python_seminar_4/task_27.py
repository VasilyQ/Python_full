# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells
#  sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

text1 = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''
n = text1.replace('.', ' ').replace('\n', ' ').lower().split(' ')
a = set(n)
print(len(a))
print(a)


# input_str = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''.replace("\'",' ').replace(".",' ').upper().split()
# print(input_str,len(set(input_str)))