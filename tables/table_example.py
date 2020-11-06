from dearpygui.core import *
from dearpygui.simple import *


# callbacks
def clear_table_call(sender, data):
    clear_table("Table##widget")


def delete_row_call(sender, data):
    delete_row("Table##widget", 6)


def delete_col_call(sender, data):
    delete_column("Table##widget", 1)


def add_row_call(sender, data):
    add_row("Table##widget", ["new1", "new2", "new3", 53])


def add_col_call(sender, data):
    add_column("Table##widget", "New Column", ["new1", "new2", "new3", "new4"])


def insert_row_call(sender, data):
    insert_row("Table##widget", 5, ["inew1", "inew2", "inew3", "inew4"])


def insert_col_call(sender, data):
    insert_column("Table##widget", 1, "Inserted Column", ["inew1", "inew2", "inew3", "inew4"])

with window("Main Window"):
    # tables
    add_button("Delete row 6", callback=delete_row_call)
    add_button("Delete col 1", callback=delete_col_call)
    add_button("Add row ", callback=add_row_call)
    add_button("Add col ", callback=add_col_call)
    add_button("Insert row 5", callback=insert_row_call)
    add_button("Insert col 1 ", callback=insert_col_call)
    add_button("Clear Table ", callback=clear_table_call)
    add_table("Table##widget", ["Column 1", "Column 2", "Column 3", "Column 4"])

    tabledata = []
    for i in range(0, 10):
        row = []
        for j in range(0, 4):
            row.append("Item" + str(i) + "-" + str(j))
        tabledata.append(row)

    set_table_data("Table##widget", tabledata)

start_dearpygui(primary_window="Main Window")
