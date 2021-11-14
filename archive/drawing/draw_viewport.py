import dearpygui.dearpygui as dpg

# creating font and back viewport drawlists
viewport_front = dpg.add_viewport_drawlist()
viewport_back = dpg.add_viewport_drawlist(front=False)

with dpg.window(label="Tutorial", width=300, height=300):
    dpg.add_text("Move the window over the drawings to see the effects.", wrap=300)
    dpg.draw_circle((100, 100), 25, color=(255, 255, 255, 255))
    dpg.draw_circle((100, 100), 25, color=(255, 255, 255, 255), parent=viewport_front)
    dpg.draw_circle((200, 200), 25, color=(255, 255, 255, 255), parent=viewport_back)

dpg.start_dearpygui()
