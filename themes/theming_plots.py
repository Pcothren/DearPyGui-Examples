import dearpygui.dearpygui as dpg
from math import sin

# creating data to use in the series
sindatax = []
sindatay = []
for i in range(0, 100):
    sindatax.append(i/100)
    sindatay.append(0.5 + 0.5*sin(50*i/100))

# You can use the style editor to test themes at runtime and find the right constants for colors and styles
dpg.show_style_editor()

# themes applied to plots REQUIRE category to be set to plots
# because plots are containers plots will propagate themes
with dpg.theme() as our_plot_theme:
    dpg.add_theme_color(dpg.mvPlotCol_PlotBg, (100, 0, 0, 50), category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_Line, (0, 255, 0, 255), category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_XAxis, (0, 255, 255, 255), category=dpg.mvThemeCat_Plots)

with dpg.theme() as series_theme:
    dpg.add_theme_color(dpg.mvPlotCol_Line, (150, 0, 100, 255), category=dpg.mvThemeCat_Plots)


with dpg.window(label="Tutorial"):

    # create plot
    with dpg.plot(label="Line Series", height=400, width=400) as plot:

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        axis_y = dpg.add_plot_axis(dpg.mvYAxis, label="y")

        # series belong to a y axis
        our_series = dpg.add_line_series((0, 1), (.5, .75), label="straight line", parent=axis_y)

dpg.set_item_theme(plot, our_plot_theme)
dpg.set_item_theme(our_series, series_theme)

dpg.start_dearpygui()