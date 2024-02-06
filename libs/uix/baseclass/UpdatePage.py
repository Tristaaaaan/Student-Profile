
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)

from database import Database

db = Database()

class UpdatePage(Screen):

    Builder.load_file('libs/uix/kv/UpdatePage.kv')

    def __init__(self, pk=None, **kw):
        super().__init__(**kw)
        self.pk = pk

    def refresh(self):
        self.ids.name.text = ''
        self.ids.grade.text = ''
        self.ids.classname.text = ''
        self.ids.school.text = ''

    def validateInfo(self):
        # Check if lengths are within the specified limits
        if not (0 < len(self.ids.name.text) <= 55) or not (0 < len(self.ids.grade.text) <= 55) or not (0 < len(self.ids.classname.text) <= 55) or not (0 < len(self.ids.school.text) <= 55):
            self.errorDialog()
            
        else:
                
            self.manager.current = 'home'
            self.manager.transition.direction = "right"

            with open(self.ids.profileImage.source, 'rb') as file:
                image_data = file.read()

            db.updateUser(self.ids.name.text, self.ids.grade.text, self.ids.classname.text, self.ids.school.text, image_data, self.pk) 
            self.refresh()




    def errorDialog(self):
        self.errorDialogRegister = MDDialog(
            MDDialogHeadlineText(
                text="Ooops!",
                halign="left",
                theme_text_color='Custom',
                text_color=[205/255, 92/255, 92/255, 1],
            ),
            MDDialogSupportingText(
                text="To proceed, kindly fill in all the information needed.",
                halign="left",
            ),
            size_hint_x=(.9),
        )

        self.errorDialogRegister.open()