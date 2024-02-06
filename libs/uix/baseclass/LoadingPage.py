from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from database import Database
from kivy.clock import Clock
db = Database()

class LoadingPage(Screen):

    Builder.load_file('libs/uix/kv/LoadingPage.kv')

    def on_enter(self):
        Clock.schedule_once(self.switch_screen, 3)  # Schedule the switch_screen method after 3 seconds

    def switch_screen(self, dt):
        # Check the DB to see if the user info is there.
        user_data = db.obtainUser()
        # User info is there. Show the home screen.
        if user_data:
            self.manager.current = 'home'
        # User information is not there. Show the registration screen.
        else:
            self.manager.current = 'register'
        # Close the DB connection.