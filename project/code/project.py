from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from random import *
import time 
from time import strftime
from datetime import datetime
from weather import Weather
import requests
from bs4 import BeautifulSoup 
import webbrowser
# from rtstock.stock import Stock
from weathercodes import codes, codes_des
import json

# all_stocks = [Stock('AAPL'),Stock('AMZN'), Stock('GOOG'), Stock('NFLX'), Stock('FB'), Stock('TSLA')]

# Find user location / current data
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)

weather = Weather()
location = weather.lookup_by_location(j['zip_code'])
print('This is the location:',location)
condition = location.condition()
forecasts = location.forecast()
astronomy = location.astronomy()

class WeatherWidget(GridLayout):

	forecast = {}
	location_label = StringProperty(str(location.title().replace('Yahoo! Weather - ','')))
	current_temp = StringProperty(str(condition['temp'] + '° ' + condition['text']))
	hi_lo = StringProperty(str(forecasts[0].low() + 'º / ' + forecasts[0].high() + 'º '))

	forecast_day_1 = StringProperty(str(datetime.strptime(forecasts[1].date(), '%d %b %Y').strftime('%a')))
	forecast_day_2 = StringProperty(str(datetime.strptime(forecasts[2].date(), '%d %b %Y').strftime('%a')))
	forecast_day_3 = StringProperty(str(datetime.strptime(forecasts[3].date(), '%d %b %Y').strftime('%a')))
	forecast_day_4 = StringProperty(str(datetime.strptime(forecasts[4].date(), '%d %b %Y').strftime('%a')))
	forecast_day_5 = StringProperty(str(datetime.strptime(forecasts[5].date(), '%d %b %Y').strftime('%a')))

	# Pull in the current weather image - uses a numeric code 
	all_codes = codes
	code_from_yahoo = int(condition['code'])
	mapped_image = all_codes.get(code_from_yahoo)[1]
	curr_image = ObjectProperty(mapped_image)

	# Load in the initial forecast images - these use a description and not a code so they need to be done differently
	all_des = codes_des

	forecast_img_1 = ObjectProperty(all_des.get(forecasts[1].text().lower()))
	forecast_img_2 = ObjectProperty(all_des.get(forecasts[2].text().lower()))
	forecast_img_3 = ObjectProperty(all_des.get(forecasts[3].text().lower()))
	forecast_img_4 = ObjectProperty(all_des.get(forecasts[4].text().lower()))
	forecast_img_5 = ObjectProperty(all_des.get(forecasts[5].text().lower()))

	# HiLo for each forecast
	forecast_hi_lo_1 = StringProperty(str(forecasts[1].low() + 'º / ' + forecasts[0].high() + 'º '))
	forecast_hi_lo_2 = StringProperty(str(forecasts[2].low() + 'º / ' + forecasts[0].high() + 'º '))
	forecast_hi_lo_3 = StringProperty(str(forecasts[3].low() + 'º / ' + forecasts[0].high() + 'º '))
	forecast_hi_lo_4 = StringProperty(str(forecasts[4].low() + 'º / ' + forecasts[0].high() + 'º '))
	forecast_hi_lo_5 = StringProperty(str(forecasts[5].low() + 'º / ' + forecasts[0].high() + 'º '))
	
	forecast_des_1 = StringProperty(forecasts[1].text())
	forecast_des_2 = StringProperty(forecasts[2].text())
	forecast_des_3 = StringProperty(forecasts[3].text())
	forecast_des_4 = StringProperty(forecasts[4].text())
	forecast_des_5 = StringProperty(forecasts[5].text())

	local_news_0 = StringProperty('')
	local_news_1 = StringProperty('')
	local_news_2 = StringProperty('')
	local_news_3 = StringProperty('')
	local_news_4 = StringProperty('')
	local_news_5 = StringProperty('')


	# Initialize the settings for the clock
	TimeSeconds = StringProperty('')
	TimeMinutes = StringProperty('')
	TimeHours = StringProperty('')

	def current_date(self):
		return time.strftime('%a %b %d')

	def get_weather_image(self):
		all_codes = codes
		code_from_yahoo = int(condition['code'])
		mapped_image = all_codes.get(code_from_yahoo)[1]
		return mapped_image

	def get_location(self):
		return location.title().replace('Yahoo! Weather - ','')

	def sunrise(self):
		return 'Sunrise: ' + astronomy.get('sunrise')

	def sunset(self):
		return 'Sunset: ' + astronomy.get('sunset')

	def update(self, dt):
		current_time = time.localtime()
		hour = current_time.tm_hour
		if hour >= 12: 
			hour = hour - 12
		self.TimeHours = str(hour).zfill(2)
		self.TimeMinutes = str(current_time.tm_min).zfill(2)
		self.TimeSeconds = str(current_time.tm_sec).zfill(2)

	def pull_site(self, site):
		url = site 
		response = requests.get(url)
		soup = BeautifulSoup(response.content, features = 'xml')
		items = soup.findAll('item')
		return items

	def pull_site_sorted(self, site):
		items = self.pull_site(site)
		stories = [(datetime.strptime(item.pubDate.text, '%a, %d %b %Y %H:%M:%S EST'), 
					item.title.text, 
					item.description.text, item.link.text) for item in items]
		stories.sort(key = lambda tup: tup[0], reverse = True)
		return stories

	def quote_of_the_day(self):
		items = self.pull_site('http://feeds.feedburner.com/brainyquote/QUOTEBR')
		return items[0].description.text + '  -' +items[0].title.text

	def top_world_news_title(self, story_num):
		items = self.pull_site_sorted('http://www.wsj.com/xml/rss/3_7085.xml')
		return items[story_num][1]

	def top_world_news_story(self, story_num):
		items = self.pull_site_sorted('http://www.wsj.com/xml/rss/3_7085.xml')
		return items[story_num][2]

	def top_world(self, story_num, field):
		items = self.pull_site_sorted('http://www.wsj.com/xml/rss/3_7085.xml')
		if field == 'title':
			return items[story_num][1]
		elif field == 'des':
			if items[story_num][0].hour >= 12: 
				hour_pub = items[story_num][0].hour - 12
			else: 
				hour_pub = items[story_num][0].hour
			min_pub = items[story_num][0].minute
			return items[story_num][2] + '['+str(hour_pub)+':'+ str(min_pub)+']'
		else: 
			return items[story_num][3]

	def top_business_title(self, story_num):
		items = self.pull_site_sorted('http://www.wsj.com/xml/rss/3_7014.xml')
		return items[story_num][1]

	def top_business_story(self, story_num):
		items = self.pull_site_sorted('http://www.wsj.com/xml/rss/3_7014.xml')
		return items[story_num][2]

	def top_business(self, story_num, field):
		items = self.pull_site_sorted('http://www.wsj.com/xml/rss/3_7014.xml')
		if field == 'title':
			return items[story_num][1]
		elif field == 'des':
			if items[story_num][0].hour >= 12: 
				hour_pub = items[story_num][0].hour - 12
			else: 
				hour_pub = items[story_num][0].hour
			min_pub = items[story_num][0].minute
			return items[story_num][2] + '['+str(hour_pub)+':'+ str(min_pub)+']'
		else: 
			return items[story_num][3]

	# def stock_symbol(self, stock):
	# 	return Stock(stock).get_ticker()

	# def stock_last_price(self, stock):
	# 	return Stock(stock).get_latest_price()

	def location_update(self):
		try: 
			location = weather.lookup_by_location(self.zip_code_input.text)
			if location is None: 
				location =  weather.lookup_by_location('10128')
		except:
			location = weather.lookup_by_location('10128')

		condition = location.condition()
		forecasts = location.forecast()
		astronomy = location.astronomy() 
		condition = location.condition()

		def current_location(location):
			return location.title().replace('Yahoo! Weather - ','')

		def current_temperature(conditon):
			return condition['temp'] + '° ' + condition['text']

		def forecast_image(day_num, forecasts):
			all_codes = codes_des
			if all_codes.get(forecasts[day_num].text().lower()) is None:  
				return 'unavailable.png'
			return all_codes.get(forecasts[day_num].text().lower())

			# day_num is an integer where 0 = today
		def high_low_temp(day_num, forecasts):
			return forecasts[day_num].low() + 'º / ' + forecasts[day_num].high() + 'º '

		def forecast_day(day_num, forecasts):
			return datetime.strptime(forecasts[day_num].date(), '%d %b %Y').strftime('%a')

		def forecast_des(day_num, forecasts):
			return forecasts[day_num].text()

		def get_google_local_rss_feed(location, story_num):
			main_url = 'https://news.google.com/news/section?output=rss&q='
			location = location.description().replace('Yahoo! Weather for ','').replace(', ','%20').replace(' ','%20')
			full_url = main_url + location
			all_stories = []
			for story in self.pull_site(full_url)[1:]:
				all_stories.append(story.title.text)
			return all_stories[story_num]

		# Update the current info
		self.location_label = current_location(location)
		self.current_temp = current_temperature(condition)
		self.hi_lo = high_low_temp(0, forecasts)

		all_codes = codes
		code_from_yahoo = int(condition['code'])
		mapped_image = all_codes.get(code_from_yahoo)[1]
		self.curr_image = mapped_image

		self.forecast_day_1 = datetime.strptime(forecasts[1].date(), '%d %b %Y').strftime('%a')
		self.forecast_img_1 = forecast_image(1, forecasts)
		self.forecast_des_1 = forecast_des(1, forecasts)
		self.forecast_hi_lo_1 = high_low_temp(1, forecasts)

		self.forecast_day_2 = datetime.strptime(forecasts[2].date(), '%d %b %Y').strftime('%a')
		self.forecast_img_2 = forecast_image(2, forecasts)
		self.forecast_des_2 = forecast_des(2, forecasts)
		self.forecast_hi_lo_2 = high_low_temp(2, forecasts)

		self.forecast_day_3 = datetime.strptime(forecasts[3].date(), '%d %b %Y').strftime('%a')
		self.forecast_img_3 = forecast_image(3, forecasts)
		self.forecast_des_3 = forecast_des(3, forecasts)
		self.forecast_hi_lo_3 = high_low_temp(3, forecasts)

		self.forecast_day_4 = datetime.strptime(forecasts[4].date(), '%d %b %Y').strftime('%a')
		self.forecast_img_4 = forecast_image(4, forecasts)
		self.forecast_des_4 = str(forecast_des(4, forecasts))
		self.forecast_hi_lo_4 = high_low_temp(4, forecasts)

		self.forecast_day_5 = datetime.strptime(forecasts[5].date(), '%d %b %Y').strftime('%a')
		self.forecast_img_5 = forecast_image(5, forecasts)
		self.forecast_des_5 = str(forecast_des(5, forecasts))
		self.forecast_hi_lo_5 = high_low_temp(5, forecasts)

		self.local_news_0 = get_google_local_rss_feed(location, 0)
		self.local_news_1 = get_google_local_rss_feed(location, 1)
		self.local_news_2 = get_google_local_rss_feed(location, 2)
		self.local_news_3 = get_google_local_rss_feed(location, 3)
		self.local_news_4 = get_google_local_rss_feed(location, 4)
		self.local_news_5 = get_google_local_rss_feed(location, 5)

	# def transit_alerts(self):
	# 	items = self.pull_site('http://www.njtransit.com/rss/RailAdvisories_feed.xml')
	# 	relevant_alerts = []
	# 	for item in items:
	# 		if 'NEC' in item.link.text:
	# 			relevant_alerts.append(item.description.text)
	# 	return '\n-'.join(relevant_alerts)

	def nba_scores(self):
		items = self.pull_site('https://www.scorespro.com/rss2/live-basketball.xml')
		all_games = []
		for item in items:
			if ('USA-NBA') in item.title.text:
				all_games.append(item.title.text.replace('#Basketball #Livescore @ScoresPro: (USA-NBA) #','').replace('#', ''))
		if all_games == []:
			return 'No recent NBA scores.'
		return '\n'.join(all_games)

	def nfl_scores(self):
		items = self.pull_site('https://www.scorespro.com/rss2/live-football.xml')
		all_games = []
		for item in items:
			# if ('USA-FBS') in item.title.text:
				# all_games.append(item.title.text.replace('American Football #Livescore @ScoresPro: (USA-FBS) #','').replace('#', ''))
			if ('USA-NFL') in item.title.text:
				all_games.append(item.title.text.replace('American Football #Livescore @ScoresPro: (USA-NFL) #','').replace('#', ''))
		if all_games == []:
			return 'No recent NFL scores.'
		return '\n'.join(all_games)

class DailyViewApp(App):
    def build(self):
    	weather_widget = WeatherWidget()
    	Clock.schedule_interval(weather_widget.update, 1)
    	return weather_widget

if __name__ == '__main__':
    DailyViewApp().run()
