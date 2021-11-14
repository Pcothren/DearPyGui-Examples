import dearpygui.dearpygui as dpg

def print_me(sender):
    print(f"Menu Item: {sender}")

with dpg.window(label="Tutorial"):

    with dpg.menu_bar():

        with dpg.menu(label="File"):

            dpg.add_menu_item(label="Save", callback=print_me)
            dpg.add_menu_item(label="Save As", callback=print_me)

            with dpg.menu(label="Settings"):

                dpg.add_menu_item(label="Setting 1", callback=print_me)
                dpg.add_menu_item(label="Setting 2", callback=print_me)

        dpg.add_menu_item(label="Help", callback=print_me)

        with dpg.menu(label="Widget Items"):

            dpg.add_checkbox(label="Pick Me", callback=print_me)
            dpg.add_button(label="Press Me", callback=print_me)
            dpg.add_color_picker(label="Color Me", callback=print_me)

dpg.start_dearpygui()