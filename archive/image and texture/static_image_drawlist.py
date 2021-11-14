import dearpygui.dearpygui as dpg

with dpg.texture_registry():
    image_id = dpg.add_static_texture(100, 100, [], file='SpriteMapExample.png')

def update_image(sender, app_data, user_data):
    image, controls = user_data
    kwargs = {}
    for k, v in controls.items():
        kwargs[k] = dpg.get_value(v)
    dpg.configure_item(image, **kwargs)

with dpg.window(label="Main"):
    dpg.add_text("This is an example of a image being added to a drawlist and updated", bullet=True)
    dpg.add_spacing(count=5)
    dpg.add_separator()
    dpg.add_spacing()
    with dpg.group() as control_group:
        pmin = dpg.add_slider_intx(label="pmin", default_value=[0, 125], max_value=500, size=2)
        pmax = dpg.add_slider_intx(label="pmax", default_value=[416, 509], max_value=500, size=2)
        uv_min = dpg.add_slider_floatx(label="uv_min", default_value=[0, 0], max_value=3, min_value=-3, size=2)
        uv_max = dpg.add_slider_floatx(label="uv_max", default_value=[1, 1], max_value=3, min_value=-3, size=2)
    control_items = {"pmin": pmin, "pmax": pmax, "uv_min": uv_min, "uv_max": uv_max}

    drawing = dpg.add_drawlist(width=416, height=384)
    image = dpg.draw_image(image_id, dpg.get_value(pmin), dpg.get_value(pmax), uv_min=dpg.get_value(uv_min), uv_max=dpg.get_value(uv_max))

controls = dpg.get_item_children(control_group)[1]
for item in controls:
    dpg.set_item_callback(item, update_image)
    dpg.set_item_user_data(item, (image, control_items))

dpg.start_dearpygui()
