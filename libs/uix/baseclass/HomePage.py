from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText
from kivymd.uix.card import MDCard

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

import requests
import datetime
import webbrowser

from database import Database


class ElementCard(MDCard):
    numberofContent = StringProperty()


class HomePage(Screen):

    Builder.load_file('libs/uix/kv/HomePage.kv')

    def __init__(self, **kw):
        super().__init__(**kw)
        self.prim_key = ''
        self.facebook = ''
        self.instagram = ''
        self.twitter = ''

    def on_enter(self, *args):
        Clock.schedule_once(self.dataLoad)

    def dataLoad(self, *args):

        db = Database()

        numSports = db.obtainItems('Sports')
        self.ids.sports.numberofContent = str(len(numSports))
        
        numArts = db.obtainItems('Arts')
        self.ids.arts.numberofContent = str(len(numArts))

        numClubs= db.obtainItems('Clubs')
        self.ids.clubs.numberofContent = str(len(numClubs))

        numCommService = db.obtainItems('Community Service')
        self.ids.community_service.numberofContent = str(len(numCommService))

        numAchievements = db.obtainItems('Achievements')
        self.ids.achievements.numberofContent = str(len(numAchievements))

        numClasses = db.obtainItems('Classes')
        self.ids.classes.numberofContent = str(len(numClasses))

        useData = db.obtainUser()

        for i in useData:
            self.prim_key = i[0]
            self.ids.name.text = i[1]
            self.ids.grade.text = i[2]
            self.ids.classname.text = i[3]
            self.ids.school.text = i[4]
            
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  
            filename = f"profileImage_{current_time}.png"

            # Creating a new Image File
            with open(filename, 'wb') as file:
                file.write(i[5])

            self.ids.profileImage.source = filename

            self.facebook = i[6]
            self.twitter = i[7]
            self.instagram = i[8]

        db.close_db_connection()

    def check_internet_connection(self):
        try:
            requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False
    
    def goToFacebook(self):
        if self.check_internet_connection():
            if self.facebook:
                facebook_url = self.facebook if self.facebook.startswith("https://") else "https://" + self.facebook
                webbrowser.open(facebook_url)
            else:
                self.errorDialog()
        else:
            self.manager.current = 'nointernet'
            self.manager.transition.direction = "left"

    def goToTwitter(self):
        if self.check_internet_connection():
            if self.twitter:
                twitter_url = self.twitter if self.twitter.startswith("https://") else "https://" + self.twitter
                webbrowser.open(twitter_url)
            else:
                self.errorDialog()
        else:
            self.manager.current = 'nointernet'
            self.manager.transition.direction = "left"

    def goToInstagram(self):
        if self.check_internet_connection():
            if self.instagram:
                instagram_url = self.instagram if self.instagram.startswith("https://") else "https://" + self.instagram
                webbrowser.open(instagram_url)
            else:
                self.errorDialog()
        else:
            self.manager.current = 'nointernet'
            self.manager.transition.direction = "left"

    def errorDialog(self):
        self.errorDialogRegister = MDDialog(

            MDDialogHeadlineText(
                text="Ooops!",
                halign="left",
                theme_text_color='Custom',
                text_color=[205/255, 92/255, 92/255, 1],
            ),

            MDDialogSupportingText(
                text="It seems that the URL field is empty. Please make sure to enter a valid URL before proceeding.",
                halign="left",
            ),

            size_hint_x=(.9),
        )

        self.errorDialogRegister.open()

    def goToUpdate(self):

        # Accessing the IDs in the 'UpdatePage' screen
        updatePage = self.manager.get_screen('update')

        updatePage.ids.name.text = self.ids.name.text
        updatePage.ids.grade.text = self.ids.grade.text
        updatePage.ids.classname.text = self.ids.classname.text
        updatePage.ids.school.text = self.ids.school.text
        updatePage.pk = self.prim_key
        updatePage.ids.profileImage.source = self.ids.profileImage.source
        updatePage.ids.facebook.text = self.facebook
        updatePage.ids.twitter.text = self.twitter
        updatePage.ids.instagram.text = self.instagram

        self.manager.transition.direction = "left"
        self.manager.current = 'update'
        
    def viewDetails(self, category):

        # Accessing the 'Category' ID in the ViewDetailsPage
        detailScreen = self.manager.get_screen('view')
        detailScreen.ids.category.text = category.text

        self.manager.current = 'view'
        self.manager.transition.direction = "left"
    