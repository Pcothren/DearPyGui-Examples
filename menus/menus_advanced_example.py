from dearpygui.core import *
from dearpygui.simple import *


# callbacks
def hide_menu(sender, data):
    hide_item("Tools")


def show_menu(sender, data):
    show_item("Tools")


def change_callback(sender, data):
    callback_name=get_item_callback("Show Docs")
    print(callback_name)
    if callback_name == show_docs:
        set_item_callback("Show Docs", show_metrics_call)
    else:
        set_item_callback("Show Docs", show_docs)


def show_docs(sender, data):
    show_documentation()


def show_metrics_call(sender, data):
    show_metrics()


def add_themes(sender, data):
    with menu("Themes", parent="MenuBar"):
        pass
    add_color_picker4("Color Selector", source="color1", parent="Themes")
    add_color_edit4("Color Item", source="color1", parent="Themes")
    show_item("Delete Themes")
    hide_item("Add Themes")


def delete_themes(sender, data):
    delete_item("Themes")
    delete_item("Color Item")
    show_item("Add Themes")
    hide_item("Delete Themes")

with window("Main Window"):
    with menu_bar("MenuBar"):
        with menu("Show/Hide"):
            add_menu_item("Show Tools", callback=show_menu)
            add_menu_item("Hide Tools", callback=hide_menu)
            add_menu_item('Change "Show Docs" Callback', callback=change_callback)
            with tooltip('Change "Show Docs" Callback', "tooltip1"):
                add_dummy(width=150)  # this is because the popup doesnt have a width to set
                add_text('this will change the "show Docs" callback to a show metrics callback')
            with menu("Empty Menu"):
                add_menu_item("Nothing")
        with menu("Tools"):
            add_menu_item("Show Docs", callback=show_docs)
            with menu("Add/Remove"):
                add_menu_item("Add Themes", callback=add_themes)
                add_menu_item("Delete Themes", callback=delete_themes)
                hide_item("Delete Themes")

    add_text("This menu bar demonstrates:")
    add_text('standard menu bar, menus, and menu items', bullet=True)
    add_text('adding menus to menus', bullet=True)
    add_text('showing and hiding the "Tools menu"', bullet=True)
    add_text("changing the callback of an already existing menu item", bullet=True)
    add_text("adding and deleting menus, menu items, app widgets from a menu item", bullet=True)
    add_text("placing a widget into the menu that controlling another widget on the body of the app", bullet=True)
    add_spacing(count=50)

start_dearpygui(primary_window="Main Window")
