import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import re

http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#first pull in the main data 
main_site = 'http://fftoday.com/stats/playerstats.php?Season=2017&GameWeek=Season&PosID=20&LeagueID='

response = http.request('GET', main_site)
soup = BeautifulSoup(response.data,'lxml')

#look through to find the Theory section
# player_lines = soup.findAll("td", {"class" : "sort1"})
table = soup.find_all('table')[3]

x = table.find_all('tr')
print(x)

x = table.findAll("tr", {"class" : "sort1"})
z = 0
for i in x: 
	line = i.findAll("td")
	for l in line: 
		print(l.get_text())
