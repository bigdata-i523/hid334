from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from random import *
import time 
# In the kv file, everything to the right of the colon is pure python
# for loading python module in kv file, use format of #:  import keyword module_name

class WeatherWidget(GridLayout):
	TimeSeconds = StringProperty('')
	TimeMinutes = StringProperty('')
	TimeHours = StringProperty('')

	def printing_test(self):
		return 'This is a test'

	def update(self, dt):
		current_time = time.localtime()
		self.TimeHours = str(current_time.tm_hour - 12).zfill(2)
		self.TimeMinutes = str(current_time.tm_min).zfill(2)
		self.TimeSeconds = str(current_time.tm_sec).zfill(2)

class DailyViewApp(App):
    def build(self):
    	weather = WeatherWidget()
    	Clock.schedule_interval(weather.update, 1)
    	return weather

if __name__ == '__main__':
    DailyViewApp().run()
