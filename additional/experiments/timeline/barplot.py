import requests
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/bigdata-i523/hid334/master/additional/experiments/timeline/timeline.txt'
response = requests.get(url)
url_data = response.text

data_dict = {}
for i in url_data.splitlines():
    line = i.split(' : ')
    data_dict[line[0]] = eval(line[1])

df = pd.DataFrame.from_dict(data_dict, orient='index')

x = pd.DataFrame.from_dict({k:dict(v) for k,v in data_dict.items()}, orient='index')

weeks = x.columns.values
sums = [x[i].sum() for i in weeks]
sns.barplot(weeks, sums, color="blue")

plt.xlabel('Week Number')
plt.ylabel('Commits')
plt.title('Commits by Week')
plt.show()
