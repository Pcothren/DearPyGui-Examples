from dearpygui.core import *
from dearpygui.simple import *

with window("Main"):
    add_text("This is an example of a image as an item", bullet=True)
    add_spacing(count=5)
    add_separator()
    add_spacing()
    add_image("canvas", "SpriteMapExample.png")

start_dearpygui(primary_window="Main")