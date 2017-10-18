import requests
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import numpy as np

url = 'https://raw.githubusercontent.com/bigdata-i523/hid334/master/additional/experiments/timeline/timeline.txt'
response = requests.get(url)
url_data = response.text

data_dict = {}
for i in url_data.splitlines():
    line = i.split(' : ')
    data_dict[line[0]] = eval(line[1])

df = pd.DataFrame.from_dict(data_dict, orient='index')

x = pd.DataFrame.from_dict({k:dict(v) for k,v in data_dict.items()}, orient='index')

g = sns.heatmap(x, annot=True, annot_kws={"size": 7})
g.set_yticklabels(g.get_yticklabels(), rotation = 0, fontsize = 8)
plt.xlabel('Week Number')
plt.ylabel('User', rotation = 0)
plt.title('Commits by Week for All Users')
plt.show()
