from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget
from database import Database

db = Database()

class RegisterPage(Screen):

    Builder.load_file('libs/uix/kv/RegisterPage.kv')

    # def switch(self):
    #     # Access the 'lezg' id in the 'second' screen
    #     second_screen = self.manager.get_screen('second')
    #     second_screen.ids.lezg.text = 'hel'
    #     self.manager.current = 'second'

    def validateInfo(self):
        # Check if lengths are within the specified limits
        if not (0 < len(self.ids.name.text) <= 55) or not (0 < len(self.ids.grade.text) <= 55) or not (0 < len(self.ids.classname.text) <= 55) or not (0 < len(self.ids.school.text) <= 55):
            self.errorDialog()
        else:

            homePage = self.manager.get_screen('home')
            homePage.ids.name.text = self.ids.name.text
            homePage.ids.grade.text = self.ids.grade.text
            homePage.ids.school.text = self.ids.school.text
            self.manager.current = 'home'
            db.addUser(self.ids.name.text, self.ids.grade.text, self.ids.classname.text, self.ids.school.text)
            self.refresh()


    def errorDialog(self):
        self.errorDialogRegister = MDDialog(
            MDDialogHeadlineText(
                text="Ooops!",
                halign="left",
            ),
            MDDialogSupportingText(
                text="To proceed, kindly fill in all the information needed.",
                halign="left",
            ),
        )

        self.errorDialogRegister.open()

    def refresh(self):
        self.ids.name.text = ''
        self.ids.grade.text = ''
        self.ids.classname.text = ''
        self.ids.school.text = ''