a = 'H'
b = 'Q'
string = ''

text = 'D:/python/python_lesson_4/text.txt'

data = open(text, 'r')
for line in data:
    string+= line
data.close

string = string.replace(a, b)

data = open(text, 'w')
data.writelines(string)
data.close()




