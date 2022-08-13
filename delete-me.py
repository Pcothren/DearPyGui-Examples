import dearpygui.dearpygui as dpg
dpg.create_context()
dpg.create_viewport(title='Test', width=600, height=600)
with dpg.window(width=500, height=500) as win:
    dates = [1546300800, 1546387200, 1546473600]
    opens = [1284.7, 1319.9, 1318.7]
    highs = [1284.75, 1320.6, 1327]
    lows = [1282.85, 1315, 1318.7]
    closes = [1283.35, 1315.3, 1326.1]

    with dpg.plot(label="Candle Series", height=400, width=-1):
        dpg.add_plot_legend()
        xaxis = dpg.add_plot_axis(dpg.mvXAxis, label="Day", time=True)
        with dpg.plot_axis(dpg.mvYAxis, label="USD"):
            dpg.add_candle_series(dates, opens, closes, lows, highs, label="GOOGL")
            dpg.fit_axis_data(dpg.top_container_stack())
        dpg.fit_axis_data(xaxis)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()