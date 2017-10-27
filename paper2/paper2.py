from tkinter import *
import requests
from bs4 import BeautifulSoup 
from weather import Weather

root = Tk()
root.geometry("1000x1000")

weather = Weather()

location = weather.lookup_by_location('metuchen, nj')
condition = location.condition()

# Get weather forecasts for the upcoming days.

forecasts = location.forecast()
astronomy = location.astronomy()

Label(root, text = condition['temp'] + '° ' +condition['text'], fg = 'white', bg = 'black', font = ('Calibri',17,'bold')).grid(row=0,column = 5, sticky = 'NE')
Label(root, text = 'Sunrise: ' + astronomy.get('sunrise'), fg = 'grey', bg = 'black', font = ('Calibri',7)).grid(row=1,column = 5, sticky = 'NE')
Label(root, text = 'Sunset: ' + astronomy.get('sunset'), fg = 'grey', bg = 'black', font = ('Calibri',7)).grid(row=2,column = 5, sticky = 'NE')

i = 0 
for forecast in forecasts:
	Label(root, text = forecast.date() + ':' + forecast.text() +' ' + forecast.low() + '/' + forecast.high(),
		fg = 'grey', bg = 'black', font = ('Calibri',6)).grid(row=5 + i ,column = 5, sticky = 'E')
	i += 1 


    # print(forecast.text())
    # print(forecast.date())
    # print(forecast.high())
    # print(forecast.low())

# for times in astronomy: 
# 	print(times.sunset)
	# print(astronomy.get('sunrise'))
	# print(astronomy.get('sunset'))


section_start = 100
url = 'http://feeds.nytimes.com/nyt/rss/Business'

response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')

items = soup.findAll('item')

root.title('Daily View')
root.configure(bg = 'black')

Label(root, text = 'Business News', fg = 'white', bg = 'black', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, sticky = 'SW')

i = section_start + 1
for item in items[:5]: 
	i +=2
	Label(root, text = item.title.text, fg = 'white', bg = 'black', font = ('Calibri',10)).grid(row = i, column = 0, sticky = 'W')
	Label(root, text = item.description.text, fg = 'grey', bg = 'black', font = ('Calibri',6)).grid(row = i+1, column = 0, sticky = 'W')


section_start = 150
url = 'http://www.espn.com/espn/rss/news'

response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')

items = soup.findAll('item')

root.configure(bg = 'black')

Label(root, text = 'Sports News', fg = 'lightblue', bg = 'black', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, sticky = 'SW')

i = section_start + 1
for item in items[:5]: 
	i +=2
	Label(root, text = item.title.text, fg = 'lightblue', bg = 'black', font = ('Calibri',8)).grid(row = i, column = 0, sticky = 'W')


url = 'https://www.scorespro.com/rss2/live-basketball.xml'
response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')

items = soup.findAll('item')
for item in items: 
	if ('USA-NBA') in item.title.text:
		x = item.title.text.replace('#Basketball #Livescore @ScoresPro: (USA-NBA) #','').replace('#', '')
		print(x)

root.mainloop()
