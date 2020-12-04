from dearpygui.core import *
from dearpygui.simple import *

def update_canvas(sender, data):
    p_min = get_value("p_min")
    p_max = get_value("p_max")
    uv_min = get_value("uv_min")
    uv_max = get_value("uv_max")
    clear_drawing("canvas") #we do this because images do not have tags that can be updated with modify_draw_command()
    draw_image("canvas", "SpriteMapExample.png", p_min, pmax=p_max, uv_min = uv_min, uv_max = uv_max)

with window("Main"):
    add_text("This is an example of a image being added to a canvas", bullet=True)
    add_spacing(count=5)
    add_separator()
    add_spacing()
    add_drawing("canvas", width=416, height=384)
    add_slider_int2("p_min", default_value=[0, 0], max_value=500)
    add_slider_int2("p_max", default_value=[416, 384], max_value=500)
    add_slider_float2("uv_min", default_value=[0,0], max_value=3, min_value=-3)
    add_slider_float2("uv_max", default_value=[1,1], max_value=3, min_value=-3)
set_render_callback(update_canvas)
start_dearpygui(primary_window="Main")
