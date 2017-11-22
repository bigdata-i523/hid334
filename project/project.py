from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from random import *
import time 
from time import strftime
from datetime import datetime
from weather import Weather
import requests
from bs4 import BeautifulSoup 
import webbrowser
from rtstock.stock import Stock

# In the kv file, everything to the right of the colon is pure python
# for loading python module in kv file, use format of #:  import keyword module_name

# Pull in the weather data
weather = Weather()
location = weather.lookup_by_location('New York, NY')
condition = location.condition()
forecasts = location.forecast()
astronomy = location.astronomy()

all_stocks = [Stock('AAPL'),Stock('AMZN'), Stock('GOOG'), Stock('NFLX'), Stock('FB'), Stock('TSLA')]


class WeatherWidget(GridLayout):

	TimeSeconds = StringProperty('')
	TimeMinutes = StringProperty('')
	TimeHours = StringProperty('')

	def current_location(self):
		return location.title().replace('Yahoo! Weather - ','')

	def current_temperature(self):
		return condition['temp'] + '° ' + condition['text']

	def current_date(self):
		return time.strftime('%a %b %d')

	# day_num is an integer where 0 = today
	def high_low_temp(self, day_num):
		return forecasts[day_num].low() + 'º / ' + forecasts[day_num].high() + 'º '

	def forecast_day(self, day_num):
		return datetime.strptime(forecasts[day_num].date(), '%d %b %Y').strftime('%a')

	def get_location(self):
		return location.title().replace('Yahoo! Weather - ','')

	def sunrise(self):
		return 'Sunrise: ' + astronomy.get('sunrise')

	def sunset(self):
		return 'Sunset: ' + astronomy.get('sunset')

	def update(self, dt):
		current_time = time.localtime()
		self.TimeHours = str(current_time.tm_hour).zfill(2)
		self.TimeMinutes = str(current_time.tm_min).zfill(2)
		self.TimeSeconds = str(current_time.tm_sec).zfill(2)

	def pull_site(self, site):
		url = site 
		response = requests.get(url)
		soup = BeautifulSoup(response.content, features = 'xml')
		items = soup.findAll('item')
		return items

	def quote_of_the_day(self):
		items = self.pull_site('http://feeds.feedburner.com/brainyquote/QUOTEBR')
		return items[0].description.text + '  -' +items[0].title.text

	def top_world_news_title(self, story_num):
		items = self.pull_site('http://www.wsj.com/xml/rss/3_7085.xml')
		return items[story_num].title.text

	def top_world_news_story(self, story_num):
		items = self.pull_site('http://www.wsj.com/xml/rss/3_7085.xml')
		return items[story_num].description.text

	def top_business_title(self, story_num):
		items = self.pull_site('http://www.wsj.com/xml/rss/3_7014.xml')
		return items[story_num].title.text

	def top_business_story(self, story_num):
		items = self.pull_site('http://www.wsj.com/xml/rss/3_7014.xml')
		return items[story_num].description.text

	def stock_symbol(self, stock):
		return Stock(stock).get_ticker()

	def stock_last_price(self, stock):
		return Stock(stock).get_latest_price()
	
	def transit_alerts(self, alert_num):
		items = self.pull_site('http://www.njtransit.com/rss/RailAdvisories_feed.xml')
		relevant_alerts = []
		for item in items:
			if 'NEC' in item.link.text:
				relevant_alerts.append(item.description.text)
		print(relevant_alerts)
		return relevant_alerts[alert_num]

class DailyViewApp(App):
    def build(self):
    	weather_widget = WeatherWidget()
    	Clock.schedule_interval(weather_widget.update, 1)
    	return weather_widget

if __name__ == '__main__':
    DailyViewApp().run()
