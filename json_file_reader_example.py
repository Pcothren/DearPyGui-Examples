from dearpygui.core import *
from dearpygui.simple import *

import json


def handle_open(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".json")

    with window("Spell Window"):
        add_text("List of Spell Names ")
    # add_window("Spell Window")
        add_same_line()
        add_label_text("##filedir", source="directory", color=[255, 0, 0])
        add_text("File: ")
        add_same_line()
        add_label_text("##file", source="json_file_to_open", color=[255, 0, 0])
        add_text("File Path: ")
        add_same_line()
        add_label_text("##filepath", source="file_path", color=[255, 0, 0])


#
# In the second part of this method you will need to change the JSON elements to match
# your JSON elements
#
def apply_selected_file(sender, data):

    directory = data[0]
    file = data[1]
    set_value("directory", directory)
    set_value("json_file_to_open", file)
    set_value("file_path", f"{directory}\\{file}")

    dir_path = get_value("directory")
    json_file = get_value("json_file_to_open")
    if json_file is not None:
        log_debug(f"file name is {json_file}")
        returned_json_file = read_json_file(dir_path + "/" + json_file)
        for spell in returned_json_file['spells']:
            spell_name = spell['name']
            add_text("Spell Name ", parent="Spell Window")
            add_same_line(parent="Spell Window")
            add_input_text(f"##spell_name_{spell_name}", default_value=spell_name, parent="Spell Window")


def read_json_file(filename):
    with open(filename) as ff:
        json_file = json.loads(ff.read())
        ff.close()
        return json_file


def print_me(sender, data):
    log_debug(f"Menu Item: {sender}")


with menu_bar("Main Menu Bar"):  # simple

    with menu("File"):  # simple
        add_menu_item("New", callback=print_me)
        add_menu_item("Open", callback=handle_open)
        add_menu_item("Save", callback=print_me)
        add_menu_item("Save As", callback=print_me)

start_dearpygui()
