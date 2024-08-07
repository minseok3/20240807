import numpy
import numpy as np
import pandas as pd

my_index = ['a','b', 'c']
my_colums = ['이름','나이','성별']
my_data = numpy.array([['Alice','bob','홍길동'],
                       [25,30,26],
                       ['남','여','남']
                       ]) .transpose()
# print(my_data)
df = pd.DataFrame(my_data,index= my_index, columns=my_colums)

#print(df[['이름','나이']]) #/열단위

print(df.loc['a'])#/행단위