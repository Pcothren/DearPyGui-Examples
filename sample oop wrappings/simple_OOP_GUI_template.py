# A simple template to create a GUI with Menu and Tab bar using classes
from dearpygui.core import *
from dearpygui.simple import *


class GuiBuilder:
    def __init__(self, width, height, theme='Dark'):
        self.theme = theme
        self.width = width
        self.height = height

    def make_gui(self):

        set_main_window_size(self.width, self.height)
        set_theme(self.theme)
        Menu()
        add_tab_bar(name='tab_bar_1', parent="Main Window")  # Parent tab bar - contains all the respective tabs
        Tab('Tab1', 'tab_bar_1').generate()
        Tab('Tab2', 'tab_bar_1').generate()

    @staticmethod
    def run_gui():
        start_dearpygui(primary_window="Main Window")


class Menu:
    # Modify the class 'Menu' to get the required structure of menu bar
    def theme_setting(sender, data):
        set_theme(data)

    with window("Main Window"):
        with menu_bar(name='Main Menu'):
            with menu(name='Menu Section 1'):
                add_menu_item('item 1')
                # add_separator()  # optional line to separate items in the menu
                add_menu_item('item 2')
            with menu(name='Menu Section 2'):
                with menu('Theme'):
                    add_menu_item('Light##Theme 1', callback=theme_setting, callback_data='Light')
                    add_menu_item('Dark##Theme 2', callback=theme_setting, callback_data='Dark')


class Tab:
    def __init__(self, tab_name, parent):
        self.tab_name = tab_name
        self.parent = parent

    def generate(self):
        with tab(name=self.tab_name, parent=self.parent):
            add_text(f'Content of {self.tab_name}')


if __name__ == '__main__':
    template = GuiBuilder(500, 500, theme='Dark')
    template.make_gui()
    template.run_gui()