from kivymd.app import MDApp

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from libs.uix.baseclass import RegisterPage
from libs.uix.baseclass import HomePage
from libs.uix.baseclass import ViewDetailsPage
from libs.uix.baseclass import LoadingPage
from libs.uix.baseclass import UpdatePage

from libs.uix.baseclass import noInternet
from libs.uix.baseclass import UserGuide

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"


class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        return WindowManager()


if __name__ == '__main__':
    rawApp().run()
