import json
import threading

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from focus.control import *

class WeaponData:
    def __init__(self, json_file_path):
        with open(json_file_path, 'r') as file:
            self.weapon_data = json.load(file)

        # Create a mapping between names and indices
        self.name_to_index = {name: index for index, name in enumerate(self.weapon_data.keys())}

    def get_data_by_name(self, name):
        return self.weapon_data.get(name, None)

    def get_data_by_position(self, position):
        name_by_position = list(self.weapon_data.keys())[position - 1]
        return self.weapon_data.get(name_by_position, None)

    def get_weapon_name_by_position(self, position):
        return list(self.weapon_data.keys())[position - 1]

class Menu:
    def __init__(self, weapon_data):
        self.weapon_data = weapon_data

    def create_ui(self):
        app = QApplication([])
        window = QWidget()
        layout = QVBoxLayout()

        weapon_selector = QComboBox()
        weapon_selector.addItems(list(self.weapon_data.weapon_data.keys()))
        weapon_selector.currentIndexChanged.connect(self.on_weapon_changed)  # Connect signal to slot

        layout.addWidget(weapon_selector)

        window.setLayout(layout)
        window.show()
        app.exec()

    def on_weapon_changed(self, index):
        selected_weapon_name = list(self.weapon_data.weapon_data.keys())[index]
        print(f"Selected weapon changed to: {selected_weapon_name}")
        
        data_by_name = self.weapon_data.get_data_by_name(selected_weapon_name)
        if data_by_name is not None:
            Control.drive_mouse(data_by_name)
        else:
            print(f"No data found for {selected_weapon_name}")

        
def main():

    # Accessing data by name
    # name = "R4C_15"
    # data_by_name = weapon_data.get_data_by_name(name)
    # if data_by_name is not None:
    #     print(f"Data for {name}: {data_by_name}")
    # else:
    #     print(f"No data found for {name}")
        
    # # Accessing data by position
    # # position = 2
    # # name_by_position = weapon_data.get_weapon_name_by_position(position)
    # # data_by_position = weapon_data.get_data_by_position(position)
    # #
    # # print(f"Data at position {position} for {name_by_position}: {data_by_position}")
        
    # mouse_thread = threading.Thread(target=Control.drive_mouse, args=(data_by_name, ))
    # mouse_thread.start()

    # mouse_thread.join()

    weapons_path = 'weapons.json'
    weapon_list = WeaponData(weapons_path)

    menu = Menu(weapon_list)
    menu.create_ui()
    

if __name__ == "__main__":
    main()