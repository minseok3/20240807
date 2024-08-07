import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg','plas', 'pres','skin','test', 'mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',names=col_names)

data.describe().to_csv('./results/describe.csv')

# print(data.describe())
plt.clf()
plt.hist(data['preg'])
plt.show()

