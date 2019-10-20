from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from database import DataBase
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.image import Image
events=[]
class WindowManager(ScreenManager):
    pass
class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    def add_to(self):
        events.insert(0,self.time.text)
        events.insert(1,self.event.text)
        events.insert(2,self.duration.text)
        print(events)
class SaveWindow(Screen):
    pass
class StudyWindow(Screen):
    pass
class ViewWindow(Screen):
    def show(self):
        ef=0
        x=0
        while True:
            self.stime.text =events[x]
            self.sevent.text =events[x+1]
            self.sduration.text =events[x+2]
            x+=3
            ef+=1
            if ef==1:
                break
class SchedulerApp(App):
    def build(self):
        return Builder.load_file("Scheduler.kv")
if __name__== "__main__":
    SchedulerApp().run()
