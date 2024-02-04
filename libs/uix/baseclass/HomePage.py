from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty

class ElementCard(MDCard):
    pass


class HomePage(Screen):

    Builder.load_file('libs/uix/kv/HomePage.kv')

    def viewDetails(self, category):

        # Access the 'category' ID in the viewDetailsPage

        detailScreen = self.manager.get_screen('view')
        detailScreen.ids.category.text = category.text

        self.manager.current = 'view'
        self.manager.transition.direction = "left"