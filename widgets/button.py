from dearpygui.core import *
from dearpygui.simple import *

def widget_editor(sender, data):
    configure_item(
        "Test Button",
        label=get_value("Label"),
        tip=get_value("Tip"),
        popup="Popup",
        show=get_value("Show"),
        enabled=get_value("Enabled"),
        width=get_value("Width"),
        height=get_value("Height"),
        small=get_value("Small"),
        arrow=get_value("Arrow"),
        direction=get_value("Direction")
    )





def autosize(sender, data):
    set_value("Width", 0)
    set_value("Height", 0)
    widget_editor(sender, data)

def fill_conatiner(sender, data):
    set_value("Width", -1)
    set_value("Height", -1)
    widget_editor(sender, data)

with window("Main Window"):
    add_input_text("Label", default_value="Test Button", callback=widget_editor)
    add_input_text("Tip", default_value="Tip", callback=widget_editor),
    add_checkbox("Show", default_value=True, callback=widget_editor)
    add_checkbox("Enabled", callback=widget_editor)
    add_slider_int("Width", default_value=0, min_value=-1, max_value=200, callback=widget_editor)
    add_slider_int("Height", default_value=0, min_value=-1, max_value=200, callback=widget_editor)
    add_checkbox("Small", callback=widget_editor)
    add_checkbox("Arrow", callback=widget_editor)
    add_slider_int("Direction", min_value=0, max_value=4, callback=widget_editor)
    add_button("Autosize", callback=autosize)
    add_button("Fill Container", callback=fill_conatiner)

    add_separator()
    add_spacing(count=10)

    add_button("Test Button",
        label=get_value("Label"),
        tip=get_value("Tip"),
        show=get_value("Show"),
        enabled=get_value("Enabled"),
        width=get_value("Width"),
        height=get_value("Height"),
        small=get_value("Small"),
        arrow=get_value("Arrow"),
        direction=get_value("Direction"))

start_dearpygui(primary_window="Main Window")
