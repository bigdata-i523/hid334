import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import numpy as np
import re
from itertools import chain


http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Pull in the main data to create a txt file
sites = ['https://www.federalreserve.gov/monetarypolicy/2017-07-mpr-summary.htm',
'https://www.federalreserve.gov/monetarypolicy/2017-07-mpr-part1.htm',
'https://www.federalreserve.gov/monetarypolicy/2017-07-mpr-part2.htm',
'https://www.federalreserve.gov/monetarypolicy/2017-07-mpr-part3.htm']

commentary = []
for site in sites: 
	response = http.request('GET', site)
	soup = BeautifulSoup(response.data,'lxml')
	commentary += soup.find_all('p')

full_text = []
words = []

for line in commentary: 
	full_text.append(line.get_text())

for text in full_text: 
	text = re.split('\n| |,|;|\.|"|\)|\(',text)
	words.append(text)

#flatten the list to be a single list 
words = list(chain.from_iterable(words))

file = open('C:\\fed_words.txt','w', encoding = 'utf-8')
file.write(" ".join(words))
file.close()
