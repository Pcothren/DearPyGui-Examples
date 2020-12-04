from dearpygui.core import *
from dearpygui.simple import *

with window("Main"):
    add_text("This is an example of a image being added to a canvas", bullet=True)
    add_spacing(count=5)
    add_separator()
    add_spacing()
    add_drawing("canvas", width=416, height=384)
    draw_image("canvas", "SpriteMapExample.png", [0, 0], pmax=[416, 384])

start_dearpygui(primary_window="Main")
