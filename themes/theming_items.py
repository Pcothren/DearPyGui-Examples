import dearpygui.dearpygui as dpg

# Themes can consist of a colors and styles

# You can use the style editor to test themes at runtime and find the right constants for colors and styles
dpg.show_style_editor()

# Create a theme container and color and styles
with dpg.theme() as our_theme:

    dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 255, 0, 255))
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 255, 255, 255))
    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0, 255))

    # Some styles use only one variable "x" and some use 2 "x,"y" looking at the style editor can help
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 20)
    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

with dpg.window(label="Tutorial", width=500, height=500):
    dpg.add_button(label="Default Theme")

    # Setting theme at start up
    our_button = dpg.add_button(label="Set At Start-up")
    dpg.set_item_theme(our_button, our_theme)

    # Themes can be set at runtime using a lambda
    dpg.add_button(label="Set Theme at Runtime", callback=lambda sender: dpg.set_item_theme(sender, our_theme))

    # Themes can be set to all items of a specific type at runtime using a callback
    def set_theme():
        dpg.set_item_type_theme(dpg.mvButton, our_theme)
    dpg.add_button(label="Theme all items of a specified type", callback=set_theme)
    dpg.add_combo(label="Combo")

dpg.start_dearpygui()