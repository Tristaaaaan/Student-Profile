from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from database import Database
from kivy.uix.modalview import ModalView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard, MDCardSwipe
from kivy.clock import Clock, mainthread
from kivymd.uix.list import MDListItem
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget

db = Database()

class ItemCard(MDBoxLayout):

    custom_title = StringProperty()
    custom_description = StringProperty()

    def __init__(self, pk=None, category=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk
        self.category = category

    def remove_item(self, instance):

        self.parent.remove_widget(instance)

        db.deleteItems(instance.pk, instance.category)
  
        self.closevalidateDeleteItem()


    def validateDeleteItem(self, instance):

        self.validateDialog = MDDialog(
            MDDialogHeadlineText(
                text=f"Delete {self.category}",
                halign="left",
            ),
            MDDialogSupportingText(
                text="By tapping 'Yes', the information you selected will be removed from your portfolio.",
                halign='left',
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="No"),
                    style="text",
                    on_release=self.closevalidateDeleteItem,
                ),
                MDButton(
                    MDButtonText(text="Yes"),
                    style="text",
                    on_release=lambda x: self.remove_item(instance),
                ),
                spacing="8dp",
            ),
            size_hint_x=(.9),
        )
        self.validateDialog.open()
    
    def closevalidateDeleteItem(self, *args):
        self.validateDialog.dismiss()


class UpdateItemDialog(MDDialog):
    
    update_custom_title = StringProperty()
    update_custom_description = StringProperty()
    headline_text = StringProperty()

    def __init__(self, pk=None, category=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk
        self.category = category

        # Add your logic for updating the item in the dialog
    def closeAddItemDialog(self):
        self.dismiss()
   
class AddItemDialog(MDDialog):

    addCategoryItem = StringProperty()

    def __init__(self, category=None, **kwargs):
        super().__init__(**kwargs)

        self.category = category

    def closeAddItemDialog(self, instance):
        instance.dismiss()

    def removeAddItemDialog(self):
        self.dismiss()
                 
class ViewDetailsPage(Screen):

    Builder.load_file('libs/uix/kv/ViewDetailsPage.kv')

    # def switch(self):
    #     # Access the 'lezg' id in the 'second' screen
    #     second_screen = self.manager.get_screen('second')
    #     second_screen.ids.lezg.text = 'hel'
    #     self.manager.current = 'second'

    def closesaveAddItemDialog(self, dialog_instance):
        dialog_instance.dismiss()

    def on_enter(self, *args):
        Clock.schedule_once(self.getItems)

        return super().on_enter(*args)
                                
    def getItems(self, *args):

        self.ids.container.clear_widgets()

        # Category
        category = self.ids.category.text

        if category == 'Sports':
            sportItemsDatabase = db.obtainItems(category)

            if sportItemsDatabase is not None:

                if sportItemsDatabase:

                    for items in sportItemsDatabase:
                        sportItems = ItemCard(pk=items[0], category=category, custom_title=items[1], custom_description=items[2])

                        self.ids.container.add_widget(sportItems)


                else:
                    print("List is empty")

            else:
                print("Database returned None")
        
        elif category == 'Arts':
            artsItemsDatabase = db.obtainItems(category)

            if artsItemsDatabase is not None:

                if artsItemsDatabase:

                    for items in reversed(artsItemsDatabase):
                        artItems = ItemCard(pk=items[0], category=category,custom_title=items[1], custom_description=items[2])
                        self.ids.container.add_widget(artItems, index=4)

                else:
                    print("List is empty")

            else:
                print("Database returned None")

        elif category == 'Clubs':
            clubsItemsDatabase = db.obtainItems(category)

            if clubsItemsDatabase is not None:

                if clubsItemsDatabase:

                    for items in reversed(clubsItemsDatabase):
                        clubItems = ItemCard(pk=items[0], category=category,custom_title=items[1], custom_description=items[2])
                        self.ids.container.add_widget(clubItems)

                else:
                    print("List is empty")
            else:
                print("Database returned None")

        elif category == 'Community Service':
            communityServiceItemsDatabase = db.obtainItems(category)

            if communityServiceItemsDatabase is not None:

                if communityServiceItemsDatabase:

                    for items in reversed(communityServiceItemsDatabase):
                        print(items[1])
                        communityServiceItems = ItemCard(pk=items[0], category=category,custom_title=items[1], custom_description=items[2])
                        self.ids.container.add_widget(communityServiceItems)

                else:
                    print("List is empty")

            else:
                print("Database returned None")

        elif category == 'Achievements':
            achievementItemsDatabase = db.obtainItems(category)

            if achievementItemsDatabase is not None:

                if achievementItemsDatabase:
   
                    for items in reversed(achievementItemsDatabase):

                        achievementItems = ItemCard(pk=items[0], category=category,custom_title=items[1], custom_description=items[2])
                        self.ids.container.add_widget(achievementItems)

                else:
                    print("List is empty")

            else:
                print("Database returned None")

        else:
            classItemsDatabase = db.obtainItems(category)

            if classItemsDatabase is not None:

                if classItemsDatabase:

                    for items in reversed(classItemsDatabase):
                        classItems = ItemCard(pk=items[0], category=category,custom_title=items[1], custom_description=items[2])
                        self.ids.container.add_widget(classItems)

                else:
                    print("List is empty")

            else:
                print("Database returned None")

    def addItem(self):

        # Create the ModalView
        self.addItemModalView = AddItemDialog(category=self.ids.category.text, addCategoryItem=f"Add {self.ids.category.text}")

        # Open the ModalView
        self.addItemModalView.open()

    def saveAddItemDialog(self, title, description, category):

        # If input(s) are inmplete or exceed maximum lengths

        if not (0 < len(title.text) <= 55) or not (0 < len(description.text) <= 255):

            print("INCOMPLETE or Exceeds Maximum Length")

        else:

            # Add the Data to the MDListItem
            self.ids.container.add_widget(ItemCard(custom_title=title.text, custom_description=description.text))

            # Save the Data
            db.createItem(title.text, description.text, category)
            
            self.ids.container.clear_widgets()

            self.getItems(self)

            self.closesaveAddItemDialog(self.addItemModalView)

    def saveUpdateItemDialog(self, title, description, category, prim_key):
        # If input(s) are incomplete or exceed maximum lengths
        print(category)
        if not (0 < len(title.text) <= 55) or not (0 < len(description.text) <= 255):

            print("INCOMPLETE or Exceeds Maximum Length")

        else:

            db.updateItems(title.text, description.text, category, prim_key)

            self.ids.container.clear_widgets()

            self.ids.container.add_widget(ItemCard(custom_title=title.text, custom_description=description.text))

            self.getItems(self)

            self.closesaveAddItemDialog(self.updateItemModalView)

    def updateItem(self, pk, title, description):

        print(pk)
        print(title)
        print(description)

        # Create the ModalView
        
        self.updateItemModalView = UpdateItemDialog(pk=pk, category=self.ids.category.text, headline_text=f"Update {self.ids.category.text}")

        # Access the MDTextField widgets and set their text properties
        self.updateItemModalView.ids.title.text = title
        self.updateItemModalView.ids.description.text = description

        # Open the ModalView
        self.updateItemModalView.open()
        
    def on_leave(self):
        self.ids.container.clear_widgets()
