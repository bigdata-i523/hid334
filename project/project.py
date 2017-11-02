import kivy
from time import strftime

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy import clock

class WeatherGrid(BoxLayout):
    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

class DailyViewApp(App):
    def build(self):
        return WeatherGrid()

if __name__ == '__main__':
    DailyViewApp().run()
