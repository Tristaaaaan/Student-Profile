from kivy.lang.builder import Builder

from kivymd.app import MDApp
from kivymd.uix.list import MDListItem

KV = '''
<GuitarItem>
    theme_bg_color: "Custom"
    md_bg_color: "2d4a50"

    MDListItemLeadingAvatar
        source: "avatar.png"

    MDListItemHeadlineText:
        text: "Ibanez"

    MDListItemSupportingText:
        text: "GRG121DX-BKF"

    MDListItemTertiaryText:
        text: "$445,99"

    MDListItemTrailingIcon:
        icon: "guitar-electric"


MDScreen:

    MDSliverAppbar:
        background_color: "2d4a50"
        hide_appbar: True

        MDTopAppBar:
            type: "medium"

            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "arrow-left"

            MDTopAppBarTitle:
                text: "Sliver toolbar"

            MDTopAppBarTrailingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "attachment"

                MDActionTopAppBarButton:
                    icon: "calendar"

                MDActionTopAppBarButton:
                    icon: "dots-vertical"

        MDSliverAppbarHeader:
            MDIconButton:
                icon: 'refresh'
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release:
                    root.release()

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            theme_bg_color: "Custom"
            md_bg_color: "2d4a50"
'''


class GuitarItem(MDListItem):
    ...


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        for x in range(10):
            self.root.ids.content.add_widget(GuitarItem())

    def release(self):
        print('release')
Example().run()