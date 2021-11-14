import dearpygui.dearpygui as dpg

# Because the built in logger was made completely from dpg commands you can reimplement it and customize it yourself!
class MyCustomLogger:

    def __init__(self):

        self.log_level = 0
        self._auto_scroll = True
        self.filter_id = None
        self.window_id = dpg.add_window(label="mvLogger", pos=(200, 200), width=500, height=500)
        self.count = 0
        self.flush_count = 1000
        self.level_options = {"Trace": 0, "Debug": 1, "Info": 2,  "Warning": 3, "Error": 4, "Critical": 5}

        with dpg.group(horizontal=True, parent=self.window_id):
            dpg.add_checkbox(label="Auto-scroll", default_value=True,
                             callback=lambda sender: self.auto_scroll(dpg.get_value(sender)))
            dpg.add_button(label="Clear", callback=lambda: dpg.delete_item(self.filter_id, children_only=True))
        dpg.add_input_text(label="Filter", callback=lambda sender: dpg.set_value(self.filter_id, dpg.get_value(sender)),
                           parent=self.window_id)
        dpg.add_radio_button(list(self.level_options.keys()), parent=self.window_id,
                             callback=lambda sender: self.set_level(self.level_options[dpg.get_value(sender)]))
        dpg.add_same_line(parent=self.window_id)
        self.child_id = dpg.add_child(parent=self.window_id, autosize_x=True, autosize_y=True)
        self.filter_id = dpg.add_filter_set(parent=self.child_id)

        with dpg.theme() as self.trace_theme:
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 0, 255))

        with dpg.theme() as self.debug_theme:
            dpg.add_theme_color(dpg.mvThemeCol_Text, (64, 128, 255, 255))

        with dpg.theme() as self.info_theme:
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))

        with dpg.theme() as self.warning_theme:
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 0, 255))

        with dpg.theme() as self.error_theme:
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0, 255))

        with dpg.theme() as self.critical_theme:
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0, 255))

    def auto_scroll(self, value):
        self._auto_scroll = value

    def _log(self, message, level):

        if level < self.log_level:
            return

        self.count += 1

        if self.count > self.flush_count:
            self.clear_log()

        theme = self.info_theme

        if level == 0:
            message = "[TRACE]\t\t" + message
            theme = self.trace_theme
        elif level == 1:
            message = "[DEBUG]\t\t" + message
            theme = self.debug_theme
        elif level == 2:
            message = "[INFO]\t\t" + message
        elif level == 3:
            message = "[WARNING]\t\t" + message
            theme = self.warning_theme
        elif level == 4:
            message = "[ERROR]\t\t" + message
            theme = self.error_theme
        elif level == 5:
            message = "[CRITICAL]\t\t" + message
            theme = self.critical_theme

        new_log = dpg.add_text(message, parent=self.filter_id, filter_key=message)
        dpg.set_item_theme(new_log, theme)
        if self._auto_scroll:
            scroll_max = dpg.get_y_scroll_max(self.child_id)
            dpg.set_y_scroll(self.child_id, -1.0)

    def log(self, message):
        self._log(message, 0)

    def log_debug(self, message):
        self._log(message, 1)

    def log_info(self, message):
        self._log(message, 2)

    def log_warning(self, message):
        self._log(message, 3)

    def log_error(self, message):
        self._log(message, 4)

    def log_critical(self, message):
        self._log(message, 5)

    def clear_log(self):
        dpg.delete_item(self.filter_id, children_only=True)
        self.count = 0

    def set_level(self, level):
        self.log_level = level

def log_things(sender, app_data, user_data):
    user_data.log("We can log to a trace level.")
    user_data.log_debug("We can log to a debug level.")
    user_data.log_info("We can log to an info level.")
    user_data.log_warning("We can log to a warning level.")
    user_data.log_error("We can log to a error level.")
    user_data.log_critical("We can log to a critical level.")

with dpg.window():
    logger = MyCustomLogger()
    logger.log("This is my logger. Just like an onion it has many levels.")
    dpg.add_button(label="Log to logger", callback=log_things, user_data=logger)

dpg.start_dearpygui()