from dearpygui.core import *
from dearpygui.simple import *

show_logger()

def window_editor(sender, data):
    if(does_item_exist("Test Window")):
        configure_item(
            "Test Window",
            width=get_value("Width"),
            height=get_value("Height"),
            x_pos=get_value("Start x"),
            y_pos=get_value("Start y"),
            autosize=get_value("No Autosize"),
            no_resize=get_value("No Resizable"),
            no_title_bar=get_value("No Title bar"),
            no_move=get_value("No Movable"),
            no_scrollbar=get_value("No Scroll bar"),
            no_collapse=get_value("No Collapse"),
            horizontal_scrollbar=get_value("Horizontal Scrollbar"),
            no_focus_on_appearing=get_value("No Focus on Appearing"),
            no_bring_to_front_on_focus=get_value("No Bring To Front on Focus"),
            menubar=get_value("Menubar"),
            no_close=get_value("No Close"),
            label=get_value("Label"))
    else:
        log_debug("window does not exists")

def create_window(sender, data):
    if(does_item_exist("Test Window")):
        log_debug("window already exists")
    else:
        with window(
                "Test Window",
                width=get_value("Width"),
                height=get_value("Height"),
                x_pos=get_value("Start x"),
                y_pos=get_value("Start y"),
                autosize=get_value("No Autosize"),
                no_resize=get_value("No Resizable"),
                no_title_bar=get_value("No Title bar"),
                no_move=get_value("No Movable"),
                no_scrollbar=get_value("No Scroll bar"),
                no_collapse=get_value("No Collapse"),
                horizontal_scrollbar=get_value("Horizontal Scrollbar"),
                no_focus_on_appearing=get_value("No Focus on Appearing"),
                no_bring_to_front_on_focus=get_value("No Bring To Front on Focus"),
                menubar=get_value("Menubar"),
                no_close=get_value("No Close"),
                label=get_value("Label"),
                on_close=on_window_close):

            for i in range(0, 3):
                add_button("button_row1" + str(i))
                add_same_line()
            for i in range(0, 5):
                add_button("button_row2" + str(i))
            log_debug("window already exists")

def on_window_close(sender, data):
    delete_item(sender)
    log_debug("window was deleted")

with window("Main Window"):
    add_input_text("Label", default_value="Test Window", callback=window_editor)
    add_slider_int("Width", default_value=400, min_value=-1, max_value=700, callback=window_editor)
    add_slider_int("Height", default_value=500, min_value=-1, max_value=700, callback=window_editor)
    add_slider_int("Start x", default_value=150, min_value=-1, max_value=700, callback=window_editor)
    add_slider_int("Start y", default_value=150, min_value=-1, max_value=700, callback=window_editor)
    add_button("Create New Window", callback=create_window)
    add_checkbox("No Autosize", callback=window_editor)
    add_checkbox("No Resizable", callback=window_editor)
    add_checkbox("No Movable", callback=window_editor)
    add_checkbox("No Title bar", callback=window_editor)
    add_checkbox("Menubar", callback=window_editor)
    add_checkbox("No Collapse", callback=window_editor)
    add_checkbox("No Close", callback=window_editor)
    add_checkbox("No Scroll bar", callback=window_editor)
    add_checkbox("Horizontal Scrollbar", callback=window_editor)
    add_checkbox("No Focus on Appearing", default_value=True, callback=window_editor)
    add_checkbox("No Bring To Front on Focus", callback=window_editor)

with window(
    "Test Window",
    width=get_value("Width"),
    height=get_value("Height"),
    x_pos=get_value("Start x"),
    y_pos=get_value("Start y"),
    autosize=get_value("No Autosize"),
    no_resize=get_value("No Resizable"),
    no_title_bar=get_value("No Title bar"),
    no_move=get_value("No Movable"),
    no_scrollbar=get_value("No Scroll bar"),
    no_collapse=get_value("No Collapse"),
    horizontal_scrollbar=get_value("Horizontal Scrollbar"),
    no_focus_on_appearing=get_value("No Focus on Appearing"),
    no_bring_to_front_on_focus=get_value("No Bring To Front on Focus"),
    menubar=get_value("Menubar"),
    no_close=get_value("No Close"),
    label=get_value("Label"),
    on_close=on_window_close):

    for i in range(0, 3):
        add_button("button_row1" + str(i))
        add_same_line()
    for i in range(0, 5):
        add_button("button_row2" + str(i))

start_dearpygui(primary_window="Main Window")
