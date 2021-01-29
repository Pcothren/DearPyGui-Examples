from dearpygui.core import *
from dearpygui.simple import *


# callbacks

def colormap_callback(sender, data):
    value = get_value("Colormaps")
    set_color_map("Plot", value)


def plot_callback():
    clear_plot("Plot")
    values=[]
    for i in range(101):
        values.append(i)
    add_heat_series("Plot", "heat", values, 10, 10, 0.0, 100.0)
    set_color_map("Plot", get_value("Colormaps"))

with window("Main Window"):
    with tab_bar("PlotTabBar"):
        with tab("Plot Widget"):
            add_text("Tips")
            add_text("Double click plot to scale to data", bullet=True)
            add_text("Right click and drag to zoom to an area", bullet=True)
            add_text("Double right click to open settings", bullet=True)
            add_text("Toggle data sets on the legend to hide them", bullet=True)
            add_text("Click and drag in the plot area to pan", bullet=True)
            add_text("Scroll mouse wheel in the plot area to zoom", bullet=True)
            add_text("Click and drag on an axis to just pan that dimension", bullet=True)
            add_text("Scroll mouse wheel on an axis to just scale that dimension", bullet=True)
            add_button("Plot data", callback=plot_callback)
            add_listbox("Colormaps", items=["Default", "Dark", "Pastel", "Paired", "Viridis",
                                            "Plasma", "Hot", "Cool", "Pink", "Jet"],
                       width=500, num_items=3, callback=colormap_callback)
            add_plot("Plot")

start_dearpygui(primary_window="Main Window")

