import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

def f(DataFrame_list, name):
    list_name = set(DataFrame_list)
    New_DataFrame = dict()
    for i in list_name:
        new_name = name + '_' + i
        New_DataFrame[new_name] = []
        for j in DataFrame_list:
            if i == j:
                New_DataFrame[new_name].append(1)
            else:
                New_DataFrame[new_name].append(0)
        new_name = name 
    return New_DataFrame

test = pd.DataFrame(f(data['whoAmI'], 'whoAmI'))

test.head(20)


    
    
