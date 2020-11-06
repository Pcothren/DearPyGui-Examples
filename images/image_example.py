from dearpygui.core import *
from dearpygui.simple import *


# callback
def update(sender, data):
    uvmin = get_value("uv_min")
    uvmax = get_value("uv_max")
    uvminx = uvmin[0]
    uvminy = uvmin[1]
    uvmaxx = uvmax[0]
    uvmaxy = uvmax[1]

    add_data("TextureCoordinates", [uvminx, uvminy, uvmaxx, uvmaxy])
    configure_item("image_1",
                   uv_min=[get_data("TextureCoordinates")[0], get_data("TextureCoordinates")[1]],
                   uv_max=[get_data("TextureCoordinates")[2], get_data("TextureCoordinates")[3]])
    print(get_data("TextureCoordinates"))

with window("Main Window"):
    add_slider_float2("uv_min", default_value=[0, 0], callback=update, min_value=-2, max_value=2)
    add_slider_float2("uv_max", default_value=[1, 1], callback=update, min_value=-2, max_value=2)

    add_data("TextureCoordinates", [0, 0, 1, 1])
    add_image("image_1", "SpriteMapExample.png",
              uv_min=[get_data("TextureCoordinates")[0], get_data("TextureCoordinates")[1]],
              uv_max=[get_data("TextureCoordinates")[2], get_data("TextureCoordinates")[3]])
show_logger()
start_dearpygui(primary_window="Main Window")
