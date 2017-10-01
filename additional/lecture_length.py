import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import re

http = urllib3.PoolManager()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#first pull in the main data 
main_site = 'https://cloudmesh.github.io/classes/i523/2017/'

response = http.request('GET', main_site)
soup = BeautifulSoup(response.data,'lxml')

#look through to find the Theory section
sections = soup.findAll("li", {"class" : "toctree-l2"})

#create an empty list to store all of the different Theory lectures so we can loop through them
theory_sites = []

#collect the interal references for the lectures so we can visit them to find the times
for section in sections: 
	for a in set(soup.findAll('a', href=True)):
			#only look at the links that are relevant to the Theory section
    		if 'course/' in a['href'] and 'course/index' not in a['href']:
    			theory_sites.append(a['href'])

#create empty lists for the Theory section names and their respective times so we can record 
#their values and summarize later
section_titles = []
section_times = []	

#the ul tag creates redudancy in the number of reported Theory sites - we just need the unique values
theory_sites = set(theory_sites)

# move to the specific theory site to find the total time
for theory in theory_sites:
	
	#reset all the time counts to begin counting for this lecture
	total_time_seconds = 0  
	all_hours, all_minutes, all_seconds = [], [], []

	#go to the specific lecture site from the main page
	url = main_site + theory

	response = http.request('GET', url)
	soup = BeautifulSoup(response.data,'lxml')

	#all of the video times are in a list format on the respective lectures - find those tags
	all_files = soup.find_all('li')

	#in the health informatics section, 3.4.1.2 - 3.4.1.7 are not formatted as bullets so 
	#we need to create a one off to account for them (they are in paragraph tags)	
	#3.4.1.5 and 3.4.1.2 are duplicate links, but values are still counted
	if theory == 'course/health.html':
			all_files += soup.find_all('p')

	#record the lecture's title
	page_title = soup.find('h1').text
	section_titles.append(page_title[:-1])

	#loop through the listed elements on the website
	for file in all_files: 
		for x in file: 
			if 'Video' in x: #differentiates from the 'Resources' link
				if 'Video 1: ' in x or 'Video 2: ' in x or 'Video 3: ' in x: #roman numerial numbering would alleviate
					x = x[:5] + x[7:]		
				time = re.findall(r'(\d+)',x[:20]) #this line could be improved (gets caught with years in title)

				#screen in case a video is in hh:mm:ss format while others are in mm:ss
				if len(time) == 3: 
					hours, minutes, seconds = time[0], time[1], time[2]
				else:
					hours, minutes, seconds = 0, time[0], time[1]

				all_hours.append(int(hours))
				all_minutes.append(int(minutes))
				all_seconds.append(int(seconds))

	#aggregate the data and convert to numeric
	all_hours = [int(i) for i in all_hours]
	all_minutes = [int(i) for i in all_minutes]
	all_seconds = [int(i) for i in all_seconds]

	total_time_seconds = sum(all_hours)*3600 + sum(all_minutes)*60 + sum(all_seconds)

	m, s = divmod(total_time_seconds, 60)
	h, m = divmod(m, 60)
	#make a reader friendly format
	section_time = "%d:%02d:%02d" % (h, m, s)

	section_times.append(section_time)

#summarize results
summary = pd.DataFrame({'Section':section_titles,'Total Time':section_times})
summary.set_index('Section',inplace=True)
summary.sort_index(inplace=True) #sorting could use improvement - currently reads 3.1 > 3.10 > 3.2
print(summary)

response.release_conn()
