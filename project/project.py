from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from random import *
import time 
from weather import Weather

# In the kv file, everything to the right of the colon is pure python
# for loading python module in kv file, use format of #:  import keyword module_name

# Pull in the weather data
weather = Weather()
location = weather.lookup_by_location('New York, NY')
condition = location.condition()
forecasts = location.forecast()
astronomy = location.astronomy()

class WeatherWidget(GridLayout):
	TimeSeconds = StringProperty('')
	TimeMinutes = StringProperty('')
	TimeHours = StringProperty('')

	def current_location(self):
		return location.title().replace('Yahoo! Weather - ','')

	def current_temperature(self):
		return condition['temp'] + '° ' +condition['text']

	def update(self, dt):
		current_time = time.localtime()
		self.TimeHours = str(current_time.tm_hour).zfill(2)
		self.TimeMinutes = str(current_time.tm_min).zfill(2)
		self.TimeSeconds = str(current_time.tm_sec).zfill(2)

class DailyViewApp(App):
    def build(self):
    	weather = WeatherWidget()
    	Clock.schedule_interval(weather.update, 1)
    	return weather

if __name__ == '__main__':
    DailyViewApp().run()
