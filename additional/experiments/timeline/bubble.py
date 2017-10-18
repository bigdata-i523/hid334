import requests
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import numpy as np

######## INPUT AREA ####################################
# This is only relevant for the single user bubble chart
custom_user = 'Adam Gonzalez'
#########################################################

url = 'https://raw.githubusercontent.com/bigdata-i523/hid334/master/additional/experiments/timeline/timeline.csv'
response = requests.get(url)
url_data = response.text

data_dict = {}
for i in url_data.splitlines():
    line = i.split(' : ')
    data_dict[line[0]] = eval(line[1])

df = pd.DataFrame.from_dict(data_dict, orient='index')

x = pd.DataFrame.from_dict({k:dict(v) for k,v in data_dict.items()}, orient='index')

user_data = x[x.index ==custom_user]
weeks = [i for i in x.columns.values]

plt.scatter(weeks,[0 for i in range(len(user_data.transpose()))], s = user_data.transpose()*100)
plt.xlim((min(weeks))-0.5, max(weeks)+0.5)
plt.xlabel('Week Number')

frame = plt.gca()
frame.axes.get_yaxis().set_visible(False)

plt.title('Commits by Week for ' + custom_user)

for i in weeks:
    value = user_data.loc[custom_user,i]
    try:
        value = int(value)
    except:
        value = 0
    plt.annotate(value, xy=(i, 0), xytext=(i, 0), ha='center', va='center', color = 'azure')
plt.show()
