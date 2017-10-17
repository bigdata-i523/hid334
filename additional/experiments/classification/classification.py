import requests
import pandas as pd
import re

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


url = "https://raw.githubusercontent.com/bigdata-i523/hid334/master/additional/experiments/classification/classification.txt"
data = requests.get(url).text

data = re.split('\n|, ',data)
pairs = [i.split(' ') for i in data]
pairs = pairs[:-1]


times, cats = [],[]

for i in pairs: 
    times.append(pd.to_numeric(i[0]))
    cats.append(pd.to_numeric(i[1]))

df = pd.DataFrame({'Time':times, 'Category':cats})
grouped = df.groupby('Category').sum()

sns.set()
g = sns.boxplot(x=cats,y=times)

g.set_title('Experiment: Classification')
g.set_xlabel("Category")
g.set_ylabel("Time Spent for Corrections")
plt.show()
print(sums)

sns.countplot(y = cats, orient = 'v')
plt.show()
