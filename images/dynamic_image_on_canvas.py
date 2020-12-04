from dearpygui.core import *
from dearpygui.simple import *

def update_canvas(sender, data):
    clear_drawing("canvas") #we do this because images do not have tags that can be updated with modify_draw_command()
    draw_image("canvas", "SpriteMapExample.png", [0, 0], pmax=[416, 384])

with window("Main"):
    add_text("This is an example of a image being added to a canvas", bullet=True)
    add_spacing(count=5)
    add_separator()
    add_spacing()
    add_drawing("canvas", width=416, height=384)
    add_button("update", callback=update_canvas)
    add_slider_int2("p_min", callback=update_canvas)
    add_slider_int2("p_max", callback=update_canvas)
    add_slider_int2("uv_min", callback=update_canvas)
    add_slider_int2("uv_max", callback=update_canvas)
start_dearpygui(primary_window="Main")
