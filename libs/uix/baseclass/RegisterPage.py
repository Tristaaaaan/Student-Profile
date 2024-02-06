from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
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
from kivymd.uix.label import MDLabel
from kivy import platform
from kivy.logger import Logger
from os.path import basename
from os.path import exists, join
from shutil import rmtree

from kivy.uix.image import Image

db = Database()


if platform == "android":
    from android.permissions import Permission, request_permissions
    from jnius import autoclass

    from androidstorage4kivy import SharedStorage, Chooser

    Environment = autoclass('android.os.Environment')
    
    request_permissions(
        [
            Permission.READ_EXTERNAL_STORAGE, 
            Permission.READ_MEDIA_IMAGES
        ]
    )

class RegisterPage(Screen):

    Builder.load_file('libs/uix/kv/RegisterPage.kv')

    # def switch(self):
    #     # Access the 'lezg' id in the 'second' screen
    #     second_screen = self.manager.get_screen('second')
    #     second_screen.ids.lezg.text = 'hel'
    #     self.manager.current = 'second'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.shared = ''
        if platform == 'android':
            # cleanup from last time if Android didn't
            temp = SharedStorage().get_cache_dir()
            if temp and exists(temp):
                rmtree(temp)

            self.chooser = Chooser(self.chooser_callback)

    # Chooser interface
    def chooser_start(self):
        self.chooser.choose_content("image/*")

    @mainthread
    def chooser_callback(self, uri_list):
        ss = SharedStorage()

        try:

            for uri in uri_list:

                self.path = ss.copy_from_shared(uri)
                print(self.path)

                self.shared = ss.copy_to_shared(self.path)

                print(self.shared)

            self.display_image(self.path)

        except Exception as e:
            print('SharedStorageExample.chooser_callback():')
            print(e)

    def display_image(self, image_path):

        if image_path:
            self.ids.profileImage.source = image_path
        else:
            print("Image path is None.")

    def validateInfo(self):
        # Check if lengths are within the specified limits
        if not (0 < len(self.ids.name.text) <= 55) or not (0 < len(self.ids.grade.text) <= 55) or not (0 < len(self.ids.classname.text) <= 55) or not (0 < len(self.ids.school.text) <= 55):
            self.errorDialog()
        else:

            self.manager.current = 'home'

            with open(self.ids.profileImage.source, 'rb') as file:
                image_data = file.read()

            db.addUser(self.ids.name.text, self.ids.grade.text, self.ids.classname.text, self.ids.school.text, image_data) 
            
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

    def refresh(self):
        self.ids.name.text = ''
        self.ids.grade.text = ''
        self.ids.classname.text = ''
        self.ids.school.text = ''