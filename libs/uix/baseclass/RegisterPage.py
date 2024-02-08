from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText

from kivy import platform
from kivy.lang import Builder
from kivy.clock import mainthread
from kivy.uix.screenmanager import Screen

from shutil import rmtree
from os.path import exists

from database import Database


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

    def __init__(self, **kw):
        super().__init__(**kw)

        if platform == 'android':
            # Cleanup from last time if Android did not
            temp = SharedStorage().get_cache_dir()

            if temp and exists(temp):
                rmtree(temp)

            self.chooser = Chooser(self.chooser_callback)

    # Chooser Type of File to View
    def chooser_start(self):
        self.chooser.choose_content("image/*")

    @mainthread
    def chooser_callback(self, uri_list):
        ss = SharedStorage()

        try:

            for uri in uri_list:

                self.path = ss.copy_from_shared(uri)
                print(self.path)

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
                
            db = Database()

            db.addUser(self.ids.name.text, self.ids.grade.text, self.ids.classname.text, self.ids.school.text, image_data, self.ids.facebook.text, self.ids.twitter.text, self.ids.instagram.text) 
            
            self.refresh()

            db.close_db_connection()
            
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
        
        self.ids.facebook.text = ''
        self.ids.instagram.text = ''
        self.ids.twitter.text = ''
