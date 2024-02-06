from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from database import Database

import threading

class LoadingPage(Screen):

    Builder.load_file('libs/uix/kv/LoadingPage.kv')

    def on_enter(self):

        Clock.schedule_once(self.switch_screen, 5)

    def switch_screen(self, dt):
        db = Database()

        # Check the DB to see if there is a User
        user_data = db.obtainUser()

        # Switch to Home if there is a User, Register if none
        if user_data:
            self.manager.current = 'home'

        else:
            self.manager.current = 'register'

        db.close_db_connection()
