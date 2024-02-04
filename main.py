from kivy.uix.screenmanager import ScreenManager
from libs.uix.baseclass import RegisterPage
from libs.uix.baseclass import HomePage
from libs.uix.baseclass import ViewDetailsPage
from kivymd.app import MDApp
from database import Database
import time

#db = Database()

class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):

        return WindowManager()


if __name__ == '__main__':
    rawApp().run()
