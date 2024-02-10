from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText

from kivy.clock import Clock
from kivy.lang import Builder

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from database import Database


class ItemCard(MDBoxLayout):

    custom_title = StringProperty()
    custom_description = StringProperty()

    def __init__(self, pk=None, category=None, **kwargs):
        super().__init__(**kwargs)
        # State a pk which we shall use link the list items with the database primary keys
        self.pk = pk
        self.category = category
    
    def remove_item(self, instance):

        self.parent.remove_widget(instance)

        db = Database()

        db.deleteItems(instance.pk, instance.category)
  
        self.closevalidateDeleteItem()
        
        db.close_db_connection()

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
                    style="filled",
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
        # State a pk which we shall use link the list items with the database primary keys
        self.pk = pk
        self.category = category

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

    def closesaveAddItemDialog(self, dialog_instance):
        dialog_instance.dismiss()

    def on_enter(self, *args):
        Clock.schedule_once(self.getItems)

        return super().on_enter(*args)
                                
    def getItems(self, *args):

        self.ids.container.clear_widgets()

        db = Database()

        # Category
        category = self.ids.category.text

        items_database = db.obtainItems(category)

        if items_database is not None:
            if items_database:
                for items in items_database:
                    item_card = ItemCard(pk=items[0], category=category, custom_title=items[1], custom_description=items[2])
                    self.ids.container.add_widget(item_card)
            else:
                print("List is empty")
        else:
            print("Database returned None")

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
                text="To proceed, kindly fill in all the information needed correctly. It must not be empty or exceed the number of characters given.",
                halign='left'
            ),

            size_hint_x=(.8),
        )

        self.errorDialogRegister.open()

    def addItem(self):

        # Create the ModalView
        self.addItemModalView = AddItemDialog(category=self.ids.category.text, addCategoryItem=f"Add {self.ids.category.text}")

        # Open the ModalView
        self.addItemModalView.open()

    def saveAddItemDialog(self, title, description, category):

        # If input(s) are inmplete or exceed maximum lengths
        if not (0 < len(title.text) <= 55) or not (0 < len(description.text) <= 255):
            self.errorDialog()

        else:
            # Add the Data to the MDListItem
            self.ids.container.add_widget(ItemCard(custom_title=title.text, custom_description=description.text))

            db = Database()

            # Save the Data
            db.createItem(title.text, description.text, category)
            
            self.ids.container.clear_widgets()

            self.getItems(self)

            self.closesaveAddItemDialog(self.addItemModalView)
        
            db.close_db_connection()

    def saveUpdateItemDialog(self, title, description, category, prim_key):

        # If input(s) are incomplete or exceed maximum lengths
        if not (0 < len(title.text) <= 55) or not (0 < len(description.text) <= 255):
            self.errorDialog()

        else:
            db = Database()

            db.updateItems(title.text, description.text, category, prim_key)

            self.ids.container.clear_widgets()

            self.ids.container.add_widget(ItemCard(custom_title=title.text, custom_description=description.text))

            self.getItems(self)

            self.closesaveAddItemDialog(self.updateItemModalView)

            db.close_db_connection()

    def updateItem(self, pk, title, description):

        # Create the ModalView
        self.updateItemModalView = UpdateItemDialog(pk=pk, category=self.ids.category.text, headline_text=f"Update {self.ids.category.text}")

        # Access the MDTextField widgets and set their text properties
        self.updateItemModalView.ids.title.text = title
        self.updateItemModalView.ids.description.text = description

        # Open the ModalView
        self.updateItemModalView.open()
        
    def on_leave(self):
        self.ids.container.clear_widgets()
