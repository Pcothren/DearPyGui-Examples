import dearpygui.dearpygui as dpg

dpg.setup_registries()

def change_text(sender, app_data, user_data):
    dpg.set_value(user_data, f"Mouse Button: {app_data[0]}, Down Time: {app_data[1]} seconds")

with dpg.window(width=500, height=300):
    text_widget = dpg.add_text("Press any mouse button")
    dpg.add_mouse_down_handler(callback=change_text, user_data=text_widget)

dpg.start_dearpygui()
