#!/usr/bin/env python
import sqlite3
from dearpygui import core, simple

# Create the database if it does not exist:
try:
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()
    print("Database created and Successfully Connected to SQLite")

except sqlite3.Error as error:
    print("File exists", error)

finally:
    if con:
        con.close()
        print("The SQLite connection is closed")

# Create the table:
try:
    con = sqlite3.connect('addresses.db')
    sqlite_create_table_query = '''CREATE TABLE address_data (
                                id INTEGER PRIMARY KEY,
                                fname TEXT,
                                sname TEXT,
                                add1 TEXT,
                                add2 TEXT,
                                add3 TEXT,
                                city TEXT,
                                pcode TEXT);'''

    cursor = con.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    con.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Table exists", error)

finally:
    if (con):
        con.close()
        print("sqlite connection is closed")


wid=500
hgt=330
core.set_main_window_size(wid, hgt)

core.add_additional_font("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Bold.otf", 25, "")


def save_callback(sender, data):

    # Store Data to variables:
    tFN = core.get_value("##fname")
    tSN = core.get_value("##sname")
    tA1 = core.get_value("##add1")
    tA2 = core.get_value("##add2")
    tA3 = core.get_value("##add3")
    tCI = core.get_value("##city")
    tPC = core.get_value("##pcode")

    # Write to table:
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()
    sqlite_insert_query = """INSERT INTO address_data
                          ( fname, sname, add1, add2, add3, city, pcode) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sqlite_insert_query, (tFN, tSN, tA1, tA2, tA3, tCI, tPC))
    con.commit()
    con.close()
    pyautogui.hotkey('tab')

    # Clear previous input data:
    tFN = core.set_value("##fname", "")
    tSN = core.set_value("##sname", "")
    tA1 = core.set_value("##add1",  "")
    tA2 = core.set_value("##add2",  "")
    tA3 = core.set_value("##add3",  "")
    tCI = core.set_value("##city",  "")
    tPC = core.set_value("##pcode", "")


with simple.window("Main Window"):
    core.add_text("")
    core.add_text("First Name:")
    core.add_same_line()
    core.add_input_text("##fname")

    core.add_text("Surname   :")
    core.add_same_line()
    core.add_input_text("##sname")

    core.add_text("Address1  :")
    core.add_same_line()
    core.add_input_text("##add1")

    core.add_text("Address2  :")
    core.add_same_line()
    core.add_input_text("##add2")

    core.add_text("Address3  :")
    core.add_same_line()
    core.add_input_text("##add3")

    core.add_text("City      :")
    core.add_same_line()
    core.add_input_text("##city")

    core.add_text("Postcode  :")
    core.add_same_line()
    core.add_input_text("##pcode", uppercase=True)

    core.add_button("Save", callback=save_callback)

# Run the script:
core.start_dearpygui(primary_window="Main Window")
