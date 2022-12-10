from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

class MainWindow(Screen):
    pass

class SurveyWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Tracker.kv")

class TrackerApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    TrackerApp().run()