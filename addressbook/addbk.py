#!/usr/bin/env python
"""
Author: Steve Fisher (xircon)
Licence: MIT
A simple python script using DearPyGui, pandas, and Sqlite3.
requires " pip install pandas"

if numpy is giving a sanity error on windows use "pip install numpy==1.19.3"

Creates a database and table in the same directory as the script.
Uses one form to do add, delete, find and edit records.
"""
import sqlite3
from dearpygui import core, simple
from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd
import sys
import csv

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
                                city TEXT,
                                pcode TEXT,
                                tel TEXT);'''

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


wid=800
hgt=600
core.set_main_window_size(wid, hgt)


def save_callback(sender, data):

    # Store Data to variables:
    tFN = core.get_value("##fname").strip()
    tSN = core.get_value("##sname").strip()
    tA1 = core.get_value("##add1").strip()
    tA2 = core.get_value("##add2").strip()
    tCI = core.get_value("##city").strip()
    tPC = core.get_value("##pcode").strip()
    tTE = core.get_value("##tel").strip()


    # Write to table:
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()
    sqlite_insert_query = """INSERT INTO address_data
                          ( fname, sname, add1, add2, city, pcode, tel) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sqlite_insert_query, (tFN, tSN, tA1, tA2, tCI, tPC, tTE))
    con.commit()
    con.close()
    clear_callback(1,1) # With dummy sender and data values. 
    table_update()
    
# Clears the Data input fields     
def clear_callback(sender, data):
    
    # Clear previous input data:
    tFN = core.set_value("##fname", "")
    tSN = core.set_value("##sname", "")
    tA1 = core.set_value("##add1",  "")
    tA2 = core.set_value("##add2",  "")
    tCI = core.set_value("##city",  "")
    tPC = core.set_value("##pcode", "")    
    tTE = core.set_value("##tel",  "")

# Finds a record based on first name and/or surname:    
def find_callback(sender, data):
    # Read first & surname: 
    tFN = core.get_value("##fname")
    tSN = core.get_value("##sname")
     
    # Connect to database:
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()

    # Find if first name and surname supplied:
    if tFN != "" and tSN != "":
       sqlite_insert_query = """SELECT * from address_data where fname LIKE ? and sname LIKE ? COLLATE NOCASE"""
       cursor.execute(sqlite_insert_query, (tFN, tSN))

    # Find if first name only supplied:
    if tFN != "" and tSN == "":
       con.set_trace_callback(print)
       sqlite_insert_query = """SELECT * from address_data where fname LIKE ? COLLATE NOCASE"""
       cursor.execute(sqlite_insert_query, (tFN,))

    # Find if only surname supplied:   
    if tFN == "" and tSN != "":
       sqlite_insert_query = """SELECT * from address_data where sname LIKE ? COLLATE NOCASE"""
       cursor.execute(sqlite_insert_query, (tSN,))

    # Return first matching record from query:       
    record = cursor.fetchone()

    # If record not found, exit, else populate fields
    if record is None:
        return
    else:
        core.set_value("##fname", record[1])
        core.set_value("##sname", record[2])
        core.set_value("##add1",  record[3])
        core.set_value("##add2",  record[4])
        core.set_value("##city",  record[5])
        core.set_value("##pcode", record[6])
        core.set_value("##tel",   record[7])
    # Close database connection:
    con.commit()
    con.close()

# Save edited data:    
def edit_callback(sender, data):
    # Populate variables:
    tFN = core.get_value("##fname")
    tSN = core.get_value("##sname")
    tA1 = core.get_value("##add1")
    tA2 = core.get_value("##add2")
    tCI = core.get_value("##city")
    tPC = core.get_value("##pcode")
    tTE = core.get_value("##tel")

    # Connect to database
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()

    # Do a quick query to the record id and prove it exists:
    sqlite_insert_query = """SELECT * from address_data where fname LIKE ? and sname LIKE ?"""
    cursor.execute(sqlite_insert_query, (tFN, tSN))

    # Get first record from query:
    exist = cursor.fetchone()
    
    # If it doesn't exist do nothing, else update record based on id:
    if exist is None:
        return
    else:
        con.set_trace_callback(print)
        sql_update = """UPDATE address_data SET add1=?, add2=?, city=?, pcode=?, tel=? WHERE id=?"""
        cursor.execute(sql_update, (tA1, tA2, tCI, tPC, tTE, exist[0]))
        con.commit()
        con.close()
    clear_callback(1,1)

# Delete record based on first & suname:
def del_callback(sender, data):
    tFN = core.get_value("##fname")
    tSN = core.get_value("##sname")

    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()

    sql_del_query = """DELETE from address_data where fname = ? AND sname = ?"""

    cursor.execute(sql_del_query, (tFN, tSN))

    con.commit()
    con.close()
    clear_callback(1,1)
    table_update()

#Update the table from a Pandas data frame
def table_update():
    # TODO Display records in table (when I work out how)!!!! 

    # Connect to database:
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()

    # Setup the query string:
    sql_sel_query = """SELECT fname, sname, tel from address_data"""

    # TODO - work out how to reference the SQL query nativeley 
    # cursor.execute(sql_sel_query)
    # records = cursor.fetchall()
    # print(records)
    # [('Mickey', 'Mouse', '0111 111 1111'), ('aaaa', 'bbbb', 'gggg'), ('Elizabeth', 'Windsor', '01 234 56789')]

    # Use Pandas to access the SQL query data
    df = pd.read_sql_query(sql_sel_query,con)
    print(df.head()) # Debug

    # Create an index to find the number of records/columns:
    index = df.index
    nrows = len(index)
    ncols = len(df.columns)

    # Populate the table from the Pandas dataframe:
    tabledata = []
    for i in range(0, nrows):
        row = []
        for j in range(0, ncols):
            row.append(df.iat[i,j])
        tabledata.append(row)

    set_table_data("Table##widget", tabledata)

    # Close the database:
    con.close()


# Export the database to a CSV using Pandas:
def export_callback(sender, data):

    # Connect to Database: 
    con = sqlite3.connect('addresses.db')
    cursor = con.cursor()

    # Setup query:
    sql_sel_query = """SELECT * from address_data"""
    # Execute
    df = pd.read_sql(sql_sel_query, con)
    # Write to CSV:
    df.to_csv('export.csv')
    
    
with simple.window("Main Window"):
    # Create the text entry input boxes:
    core.add_text("")
    core.add_text("First Name:")
    core.add_same_line()
    core.add_input_text("##fname")
    core.add_same_line()
    core.add_text("?")

    core.add_text("Surname   :")
    core.add_same_line()
    core.add_input_text("##sname")
    core.add_same_line()
    core.add_text("?")    

    core.add_text("Address1  :")
    core.add_same_line()
    core.add_input_text("##add1")

    core.add_text("Address2  :")
    core.add_same_line()
    core.add_input_text("##add2")

    core.add_text("City      :")
    core.add_same_line()
    core.add_input_text("##city")

    core.add_text("Postcode  :")
    core.add_same_line()
    core.add_input_text("##pcode", uppercase=True)

    core.add_text("Phone No  :")
    core.add_same_line()
    core.add_input_text("##tel")

    # Create the buttons:
    # Row 1
    core.add_text("")
    core.add_button("Save", callback=save_callback, tip="Enter Data click Save")
    
    # Row 2
    core.add_button("Find", callback=find_callback, tip="Enter Firstname &/or Surname, click find")
    core.add_same_line()
    core.add_button("Save Edits", callback=edit_callback, tip="Save edited record")
    core.add_same_line()
    core.add_button("Clear", callback=clear_callback, tip="Clear fields")
    core.add_same_line()
    core.add_button("Delete", callback=del_callback, tip="Delete record")
    core.add_same_line()
    core.add_button("Export", callback=export_callback, tip="Export to CSV")

    
    add_table("Table##widget", ["First Name", "Surname", "Telephone Number"])
    table_update()

 
# Run the script:
core.start_dearpygui(primary_window="Main Window")
