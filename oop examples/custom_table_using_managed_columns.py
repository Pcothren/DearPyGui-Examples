from dearpygui.core import *
from dearpygui.simple import *


class SmartTable:
    # This is the smart table that will fill widgets for cells based on type
    def __init__(self, name: str, header: List[str] = None, parent=""):
        self.name = name
        self.header = header
        self.row = 0
        self.column = 0
        self.parent = parent

        with group(self.name, parent=self.parent):
            if header is not None:
                self.add_header(self.header)
            else:
                pass

    def add_header(self, header: List[str]):
        add_separator(parent=self.name)
        with managed_columns(f"{self.name}_head", len(header), parent=self.name):
            for item in header:
                add_text(item, default_value=item)
                set_value(item, item)
        add_separator(parent=self.name)

    def add_row(self, row_content: List[Any]):
        with managed_columns(f"{self.name}_{self.row}", len(row_content), parent=self.name):
            for item in row_content:
                if type(item) is str:
                    add_input_text(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1)
                    set_value(f"##{self.name}_{self.row}_{self.column}", item)
                if type(item) is int:
                    add_input_int(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1, step=0)
                    set_value(f"##{self.name}_{self.row}_{self.column}", item)
                if type(item) is float:
                    add_input_float(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1, step=0)
                    set_value(f"##{self.name}_{self.row}_{self.column}", item)
                self.column += 1
        self.column = 0
        self.row += 1
        add_separator(parent=self.name)

    def get_cell_data(self, row: int, col: int) -> Any:
        return get_value(f"##{self.name}_{row}_{col}")

    def clear_table(self):
        if(get_item_children(self.name)):
            self.row = 0
            self.column = 0
            for item in get_item_children(self.name):
                print(item)
                if is_item_container(item):
                    for cell in get_item_children(self.name):
                        print(cell)
                        decref_value(cell)
                delete_item(item)

def refresh(sender, data):
    table_1.clear_table()
    table_1.add_header(["new", "head", "Favorite Food", "Height"])
    table_1.add_row(["test", 2345, "this", 5.3])
    table_1.add_row(["new", 2345, "is", 3.4])
    table_1.add_row(["data", 2345, "beautiful", 7.9])

def check_values(sender, data):
    log_debug(table_1.get_cell_data(1, 2))
    log_debug(table_1.get_cell_data(1, 1))

with window("Main Window"):
    add_text("This table example uses managed_columns command to create a table", bullet=True)
    add_text("Since managed columns can show widgets this table can take any item and use it as a cell item", bullet=True)

    add_spacing(count=10)

    table_1 = SmartTable("My Friends", parent="Main Window")
    table_1.add_header(["Name", "Age", "Favorite Food", "Height"])
    table_1.add_row(["stormayy", 25, "Cabbage", 5.3])
    table_1.add_row(["yantoseth", 19, "Pizza", 3.4])
    table_1.add_row(["johnpaul444", 19, "Popcorn", 7.9])
    add_button("refresh", callback=refresh)
    add_button("check values", callback=check_values)

show_logger()
start_dearpygui(primary_window="Main Window")
