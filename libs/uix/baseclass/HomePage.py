from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty
from database import Database

db = Database()

class ElementCard(MDCard):
    numberofContent = StringProperty()


class HomePage(Screen):

    Builder.load_file('libs/uix/kv/HomePage.kv')

    def on_enter(self):
        numSports = db.obtainItems('Sports')
        print(len(numSports))

        self.ids.sports.numberofContent = str(len(numSports))
        

        numArts = db.obtainItems('Arts')
        print(len(numArts))

        self.ids.arts.numberofContent = str(len(numArts))


        numClubs= db.obtainItems('Clubs')
        print(len(numClubs))

        self.ids.clubs.numberofContent = str(len(numClubs))


        numCommService = db.obtainItems('Community Service')
        print(len(numCommService))

        self.ids.community_service.numberofContent = str(len(numCommService))


        numAchievements = db.obtainItems('Achievements')
        print(len(numAchievements))

        self.ids.achievements.numberofContent = str(len(numAchievements))


        numClasses = db.obtainItems('Classes')
        print(len(numClasses))

        self.ids.classes.numberofContent = str(len(numClasses))
                                        
    def viewDetails(self, category):

        # Access the 'category' ID in the viewDetailsPage

        detailScreen = self.manager.get_screen('view')
        detailScreen.ids.category.text = category.text

        self.manager.current = 'view'
        self.manager.transition.direction = "left"
    