import dearpygui.core as dpg
import dearpygui.simple as sdpg
import uuid
from zipfile import ZipFile


class FileZipApp:
    def __init__(self):
        self.files_list = []
        self.output_directory = './'

    def __render(self, sender, data):
        """Run every frame to update the GUI.

        Updates the table by clearing it and inserting rows with the data.
        """
        dpg.clear_table('Files')
        for f in self.files_list:
            dpg.add_row('Files', [f['path'], f['name']])

    def __clear_files(self, sender, data):
        self.files_list = []

    def __remove_file(self, sender, data):
        file_row = dpg.get_table_selections("Files")
        file_index = file_row[0][0]
        self.files_list.pop(file_index)

    def __set_output_directory(self, sender, data):
        directory = data[0]
        selected_folder = data[1]
        if selected_folder in directory:
            self.output_directory = directory
        else:
            self.output_directory = '\\'.join(data)
        print(self.output_directory)
        dpg.set_value('Selected output directory:', f'Selected output directory: {self.output_directory}')

    def __select_output_directory(self, sender, data):
        dpg.select_directory_dialog(self.__set_output_directory)

    def __add_file(self, sender, data):
        is_file_unique = True

        for f in self.files_list:
            if f['name'] == data[1]:
                is_file_unique = False

        if is_file_unique:
            self.files_list.append({'path': data[0], 'name': data[1]})
        else:
            dpg.set_value('##warnings', "There are files with the same name.")

    def __select_file(self, sender, data):
        dpg.open_file_dialog(self.__add_file)

    def __zip_files(self, sender, data):
        dpg.set_value('Zip Progress', 0)
        with ZipFile(f'{self.output_directory}\\{uuid.uuid4().hex}.zip', 'w') as zip_file:
            current_progress = 0
            total_progress = len(self.files_list)
            for f in self.files_list:
                full_path = f['path'] + "\\" + f['name']
                zip_file.write(full_path, f['name'])

                # Update progress bar
                current_progress += 1
                dpg.set_value('Zip Progress', current_progress / total_progress)

    def show(self):
        """Start the gui."""
        with sdpg.window("Main Window"):
            dpg.set_main_window_size(550, 650)
            dpg.set_main_window_resizable(False)
            dpg.add_spacing()
            dpg.set_main_window_title("Dearpygui File Zip")

            dpg.add_spacing()
            dpg.add_text("File Zip App")
            dpg.add_spacing()
            dpg.add_text("Select files to zip by adding them to the table", bullet=True)
            dpg.add_text("Set the output directory", bullet=True)
            dpg.add_text("Click on the table to remove a file", bullet=True)
            dpg.add_text("Click on the zip files button to zip all the files", bullet=True)
            dpg.add_text("If you do not choose a directory, it will by default be"
                         "the same directory from where you've run this script.", bullet=True)
            dpg.add_spacing()
            dpg.add_separator()

            dpg.add_spacing(count=10)
            dpg.add_button("Select output directory", width=250, callback=self.__select_output_directory)
            dpg.add_same_line()
            dpg.add_button("Add file", width=250, callback=self.__select_file)
            dpg.add_spacing(count=10)
            dpg.add_separator()

            dpg.add_text("Selected output directory:")
            dpg.add_table('Files', ['Path', 'Name'], height=200, callback=self.__remove_file)
            dpg.add_separator()
            dpg.add_progress_bar('Zip Progress', width=-1)
            dpg.add_separator()
            dpg.add_button("Clear files", width=250, callback=self.__clear_files)
            dpg.add_same_line()
            dpg.add_button("Zip Files", width=250, callback=self.__zip_files)
            dpg.add_spacing()
            dpg.add_label_text('##warnings')

            # Render Callback and Start gui
            dpg.set_render_callback(self.__render)
            dpg.start_dearpygui(primary_window="Main Window")


if __name__ == '__main__':
    file_zip_app = FileZipApp()
    file_zip_app.show()

