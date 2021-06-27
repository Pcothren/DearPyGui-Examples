import dearpygui.dearpygui as dpg

with dpg.texture_registry():
    # we are using static textures here, however dynamic and raw textures are allowed
    image_id = dpg.add_static_texture(100, 100, [], file='../image and texture/SpriteMapExample.png')

with dpg.window(label="Tutorial"):
    with dpg.drawlist(width=700, height=700):
        dpg.draw_image(image_id, (0, 400), (200, 600), uv_min=(0, 0), uv_max=(1, 1))
        dpg.draw_image(image_id, (400, 300), (600, 500), uv_min=(0, 0), uv_max=(0.5, 0.5))
        dpg.draw_image(image_id, (0, 0), (300, 300), uv_min=(0, 0), uv_max=(2.5, 2.5))

dpg.start_dearpygui()
