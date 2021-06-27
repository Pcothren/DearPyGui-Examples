import dearpygui.dearpygui as dpg

dpg.setup_registries()

def change_text(sender, app_data, user_data):
    if (dpg.is_item_hovered(user_data)):
        dpg.set_value(user_data, f"Stop Hovering Me, Go away!!")
    else:
        dpg.set_value(user_data, f"Hover Me!")
with dpg.window(width=500, height=300):
    text_widget = dpg.add_text("Hover Me!")
    dpg.add_mouse_move_handler(callback=change_text, user_data=text_widget)

dpg.start_dearpygui()