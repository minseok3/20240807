import  pandas as pd
data = pd.Series([10,20,30,40,50], index= ["a","b","c","d","e"])
data['b'] = 60
print(data,'\n', data['b'])