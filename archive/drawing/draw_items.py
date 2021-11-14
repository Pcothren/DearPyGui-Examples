import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial"):
    with dpg.drawlist(width=300, height=300):
        dpg.draw_line((10, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)
        dpg.draw_text((0, 0), "Origin", color=(250, 250, 250, 255), size=15)
        dpg.draw_arrow((50, 70), (100, 65), color=(0, 200, 255), thickness=1, size=10)

dpg.start_dearpygui()