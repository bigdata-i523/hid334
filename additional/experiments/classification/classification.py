import requests
import pandas as pd
import re

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


url = "https://raw.githubusercontent.com/bigdata-i523/hid334/master/additional/experiments/classification.txt"
data = requests.get(url).text

data = re.split('\n|, ',data)
pairs = [i.split(' ') for i in data]
