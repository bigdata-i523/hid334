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

sns.set()
g = sns.boxplot(x=cats,y=times)

g.set_title('Experiment: Classification')
g.set_xlabel("Category")
g.set_ylabel("Time Spent for Corrections")

sns.swarmplot(x=cats,y=times, color = "0.25")
plt.show()
