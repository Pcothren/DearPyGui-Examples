from dearpygui.core import *
from dearpygui.simple import *


class SmartTable:
    # This is the smart table that will fill widgets for cells based on type
    def __init__(self, name: str, header: List[str] = None):
        self.name = name
        self.header = header
        self.row = 0
        self.column = 0

        if header is not None:
            self.add_header(self.header)

    def add_header(self, header: List[str]):
        add_separator()
        with managed_columns(f"{self.name}_head", len(header)):
            for item in header:
                add_text(item)

    def add_row(self, row_content: List[Any]):
        with managed_columns(f"{self.name}_{self.row}", len(row_content)):
            for item in row_content:
                if type(item) is str:
                    add_input_text(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1)
                if type(item) is int:
                    add_input_int(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1, step=0)
                if type(item) is float:
                    add_input_float(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1, step=0)
                self.column += 1
        self.column = 0
        self.row += 1
        add_separator()

    def get_cell_data(self, row: int, col: int) -> Any:
        return get_value(f"##{self.name}_{row}_{col}")


with window("Main Window"):
    add_text("This table example uses managed_columns command to create a table", bullet=True)
    add_text("Since managed columns can show widgets this table can take any item and use it as a cell item", bullet=True)

    add_spacing(count=10)

    table_1 = SmartTable("My Friends")
    table_1.add_header(["Name", "Age", "Favorite Food", "Height"])
    table_1.add_row(["stormayy", 25, "Cabbage", 5.3])
    table_1.add_row(["yantoseth", 19, "Pizza", 3.4])
    table_1.add_row(["johnpaul444", 19, "Popcorn", 7.9])
    log_debug(table_1.get_cell_data(1, 2))
    log_debug(table_1.get_cell_data(1, 1))

show_logger()
start_dearpygui(primary_window="Main Window")
