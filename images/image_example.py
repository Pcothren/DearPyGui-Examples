from dearpygui.core import *
from dearpygui.simple import *

show_debug()

def displayRuntime(sender, data):
    clear_drawing("canvas")
    draw_image("canvas", "SpriteMapExample.png", [0, 0], pmax=[416, 384])

with window("Main"):
    add_drawing("canvas", width=416, height=384, parent="Main")
    set_render_callback(displayRuntime)

start_dearpygui(primary_window="Main")
