from kivy.uix.screenmanager import ScreenManager
from libs.uix.baseclass import RegisterPage
from libs.uix.baseclass import HomePage
from libs.uix.baseclass import ViewDetailsPage
from kivymd.app import MDApp
from database import Database
import time
from kivy.core.window import Window

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

#db = Database()

class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):

        return WindowManager()


if __name__ == '__main__':
    rawApp().run()
