import dearpygui.dearpygui as dpg
import dearpygui.logger as dpg_logger

logger = dpg_logger.mvLogger()

dpg.show_documentation()
dpg.show_style_editor()
dpg.show_debug()
dpg.show_about()
dpg.show_metrics()
dpg.show_font_manager()
dpg.show_item_registry()

dpg.start_dearpygui() 