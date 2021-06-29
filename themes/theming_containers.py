import dearpygui.dearpygui as dpg

# You can use the style editor to test themes at runtime and find the right constants for colors and styles
dpg.show_style_editor()

# Create a theme container and color and styles
with dpg.theme() as our_theme:

    dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 255, 0, 255))
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 255, 255, 255))
    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0, 255))

    dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (100, 150, 0, 255))
    dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (0, 255, 0, 255))

    # Some styles use only one variable "x" and some use 2 "x,"y" looking at the style editor can help
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 20)
    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

# Themes applied to containers and will propagate to any children that use that theme constant
with dpg.window(label="Theme applied to child that propagates", width=300, height=300):
    dpg.add_button(label="Default Theme Because above theme")
    with dpg.child() as top_container:
        dpg.add_button(label="Button")
        dpg.add_combo(label="recursive theme Radio Button")
        with dpg.child():
            dpg.add_button(label="recursive theme Button")
            dpg.add_combo(label="recursive theme Radio Button")
    with dpg.group():
        dpg.add_button(label="Button")
        dpg.add_combo(label=" Radio Button")
    dpg.set_item_theme(top_container, our_theme)

# Themes applied to all container types will apply and propigate to all container types across windows
with dpg.window(label="Theme applied to all group containers", width=300, height=150):
    dpg.add_button(label="Default Theme Because above theme")
    with dpg.group():
        dpg.add_button(label="Button")
        dpg.add_combo(label="Radio Button")
    with dpg.group():
        dpg.add_button(label="Button")
        dpg.add_combo(label=" Radio Button")
        with dpg.group():
            dpg.add_button(label="recursive theme Button")
            dpg.add_combo(label="recursive theme Radio Button")
dpg.set_item_type_theme(dpg.mvGroup, our_theme)

# themes can be applied to whole windows
with dpg.window(label="Themed Window") as themed_window:
    dpg.add_button(label="Default Theme Because above theme")
    with dpg.child() as top_container:
        dpg.add_button(label="Button")
        dpg.add_combo(label="recursive theme Radio Button")
        with dpg.child():
            dpg.add_button(label="recursive theme Button")
            dpg.add_combo(label="recursive theme Radio Button")
dpg.set_item_theme(themed_window, our_theme)

dpg.start_dearpygui()