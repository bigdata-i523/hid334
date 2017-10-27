from tkinter import *
import requests
from bs4 import BeautifulSoup 
from weather import Weather
from datetime import datetime
import calendar
import webbrowser
# from PIL import Image, ImageTK


root = Tk()
root.geometry("1250x1250")
root.title('Daily View')
root.configure(bg = 'white')


# Pull in the weather data
weather = Weather()
location = weather.lookup_by_location('metuchen, nj')
condition = location.condition()
forecasts = location.forecast()
astronomy = location.astronomy()

dt_format='%d%m%Y'

weather_bg = 'white'

# Show the location
weather_root = Frame(root, bg = 'orange').grid(row = 0, column = 0,sticky = W)

# quote_root = Frame(root,width=1000, height =5, bg = 'red').grid(row = 6, column = 0,sticky = W+E+N+S)

# sport_root = Frame(root,width=100, height=10, bg = 'blue')
# sport_root.pack(side = TOP,  fill= BOTH)

# scores_root = Frame(root,width=100, height=10, bg = 'white')
# scores_root.pack(side = TOP,  fill= BOTH)

# football_root = Frame(root,width=100, height=10, bg = 'yellow')
# football_root.pack(side = TOP,  fill= BOTH)

# financial_root = Frame(root, bg = 'red')
# financial_root.pack(side = TOP,  fill= BOTH)

# time_root = Frame(root, bg = 'red')
# time_root.pack(side = RIGHT,  fill= BOTH)

####### PULL IN WEATHER DATA ########

# Read in the temperature
weather_start_row = 0
Label(weather_root, text = condition['temp'] + '° ' +condition['text'], fg = 'cornflowerblue', bg = weather_bg, font = ('Calibri',17,'bold')).grid(row=weather_start_row,column = 0, sticky=W)

# file_in = 'C:\\Users\\peterru\\Desktop\\weather\\sunny.png'
# pil_image = Image.open(file_in)
# image200x100 = pil_image.resize((10, 10), Image.ANTIALIAS)
# file_out = 'Roses200x100.jpg'
# image200x100.save(file_out)
# curr_weather = ImageTK.PhotoImage(PhotoImage(image200x100))
# curr_weather = curr_weather.subsample(2, 2)
# label = Label(root, image=curr_weather, borderwidth = 0, highlightthickness=0)
# label.image = curr_weather
# label.grid(row = weather_start_row+1, column = 0)

Label(weather_root, text = location.title().replace('Yahoo! Weather - ',''), fg = 'cornflowerblue', bg = weather_bg, font = ('Calibri',12)).grid(row=weather_start_row+2,column = 0,sticky=W)
Label(weather_root, text = forecasts[0].high() + ' / ' + forecasts[0].low(), fg = 'slategrey', bg = weather_bg, font = ('Calibri',12, 'bold')).grid(row=weather_start_row+3,column = 0,sticky=W)
Label(weather_root, text = 'Sunrise: ' + astronomy.get('sunrise'), fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=weather_start_row+4,column = 0,sticky=W)
Label(weather_root, text = 'Sunset: ' + astronomy.get('sunset'), fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=weather_start_row+5,column = 0,sticky=W)

j = 0 
for forecast in forecasts[1:6]:

	Label(weather_root, text = 'Image Placehold',
		fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=2,column = 1+j, sticky = 'W')

	date_given = forecast.date()
	weekday_from_date = calendar.day_name[datetime.strptime(date_given,'%d %b %Y').weekday()][:3]

	Label(weather_root, text = weekday_from_date,
		fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=3,column = 1+j)

	Label(weather_root, text = forecast.low() + '  /  ' + forecast.high(),
		fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=4,column = 1+j)

	j += 1 


# SHOW THE TIME
time_root = Frame(root, bg = 'blue').grid(row = 0, column = 7, rowspan = 4, sticky = NE)
Label(time_root, text = datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fg = 'slategrey', bg = weather_bg, font = ('Calibri',18)).grid(row=0,column = 7, rowspan = 4, sticky=NE)

#####################################

# url = 'http://feeds.feedburner.com/brainyquote/QUOTEBR'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, features = 'xml')
# items = soup.findAll('item')
# for item in items: 
# 		Label(quote_root, text = items[0].description.text + '  -' +items[0].title.text , fg = 'orange', bg = 'white', font = ('Calibri',11,'italic')).grid(row=0, column = 0, sticky= 'nw')



# #####################################

# # FILL IN THE TOP STORIES

# news_root = Frame(root, bg = 'green').grid(row = 10, column = 0,sticky = W+E+N+S)

# section_start = 0
# url = 'http://feeds.nytimes.com/nyt/rss/Business'

# response = requests.get(url)
# soup = BeautifulSoup(response.content, features = 'xml')

# items = soup.findAll('item')
# Label(news_root, text = 'Business News', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, sticky = 'W')

# i = section_start + 1
# for item in items[:5]: 
# 	i +=2
# 	Label(news_root, text = item.title.text, fg = 'mediumblue', bg = 'white', font = ('Calibri',10)).grid(row = i, column = 0, sticky = 'W')
# 	Label(news_root, text = item.description.text, fg = 'dimgray', bg = 'white', font = ('Calibri',8)).grid(row = i+1, column = 0, sticky = 'W')

# #####################################

# # FILL IN THE SPORTS 

# #####################################

# url = 'http://rss.nytimes.com/services/xml/rss/nyt/Sports.xml'

# response = requests.get(url)
# soup = BeautifulSoup(response.content, features = 'xml')

# items = soup.findAll('item')
# Label(sport_root, text = 'Sports News', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, sticky = 'W')

# i = section_start + 1
# for item in items[:5]: 
# 	i +=2
# 	Label(sport_root, text = item.title.text, fg = 'mediumblue', bg = 'white', font = ('Calibri',10)).grid(row = i, column = 0, sticky = 'W')
# 	Label(sport_root, text = item.description.text, fg = 'dimgray', bg = 'white', font = ('Calibri',8)).grid(row = i+1, column = 0, sticky = 'W')

# #######################################

# url = 'https://www.scorespro.com/rss2/live-basketball.xml'

# response = requests.get(url)
# soup = BeautifulSoup(response.content, features = 'xml')

# Label(scores_root, text = 'Live NBA Scores', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, sticky = 'W')

# items = soup.findAll('item')

# i = 0
# for item in items: 
# 	if ('USA-NBA') in item.title.text:
# 		x = item.title.text.replace('#Basketball #Livescore @ScoresPro: (USA-NBA) #','').replace('#', '')
# 		Label(scores_root, text = x, fg = 'mediumblue', bg = 'white', font = ('Calibri',10)).grid(row = i+2, column = 0, sticky = 'W')

# if i == 0: 
# 	Label(scores_root, text = 'No live NBA games currently', fg = 'darkgray', bg = 'white', font = ('Calibri',10,'italic')).grid(row = 1, column = 0, sticky = 'W')
# ###########################################

# url = 'https://www.scorespro.com/rss2/live-football.xml'

# response = requests.get(url)
# soup = BeautifulSoup(response.content, features = 'xml')

# Label(football_root, text = 'Live Football Scores', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, sticky = 'W')

# items = soup.findAll('item')

# i = 0
# for item in items: 
# 	if (('USA-FBS') or ('USA-NFL') in item.title.text) and (item.description.text != 'Match Finished'):

# 		if ('USA-FBS') in item.title.text:
# 			x = item.title.text.replace('American Football #Livescore @ScoresPro: (USA-FBS) #','').replace('#', '')

# 		elif ('USA-NFL') in item.title.text:
# 			x = item.title.text.replace('American Football #Livescore @ScoresPro: (USA-NFL) #','').replace('#', '')
			
# 		Label(football_root, text = x, fg = 'mediumblue', bg = 'white', font = ('Calibri',10)).grid(row = i+2, column = 0, sticky = 'W')
# 		i += 1 

# if i == 0: 
# 	Label(football_root, text = 'No live football games currently', fg = 'darkgray', bg = 'white', font = ('Calibri',10,'italic')).grid(row = 1, column = 0, sticky = 'W')
# ###########################################
# Label(time_root, text = 'Test', fg = 'darkgray', bg = 'white', font = ('Calibri',10,'italic')).grid(row = 0, column = 1, sticky = 'W')
root.mainloop()
