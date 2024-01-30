import threading
import time

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from focus.control import Control

class Menu(QWidget):
    def __init__(self, weapon_data):
        super().__init__()
        self.weapon_data = weapon_data
        self.mouse_thread = None

        self.init_ui()
 
    def init_ui(self):
        layout = QVBoxLayout()

        weapon_selector = QComboBox()
        weapon_selector.addItems(list(self.weapon_data.weapon_data.keys()))
        weapon_selector.currentIndexChanged.connect(self.on_weapon_changed)

        layout.addWidget(weapon_selector)

        self.setLayout(layout)

    def on_weapon_changed(self, index):
        selected_weapon_name = list(self.weapon_data.weapon_data.keys())[index]
        print(f"Selected weapon changed to: {selected_weapon_name}")

        Control.stop_mouse(True)

        if self.mouse_thread and self.mouse_thread.is_alive():
            self.mouse_thread.join()

        while threading.active_count() > 1:
            time.sleep(0.1)
        Control.stop_mouse(False)
        
        data_by_name = self.weapon_data.get_data_by_name(selected_weapon_name)
        if data_by_name is not None:
            self.mouse_thread = threading.Thread(target=Control.drive_mouse, args=(data_by_name,))
            self.mouse_thread.start()
        else:
            print(f"No data found for {selected_weapon_name}")
    
    def closeEvent(self, event: QCloseEvent):
        Control.stop_mouse(True)  # Stop the background thread before closing
        if self.mouse_thread and self.mouse_thread.is_alive():
            self.mouse_thread.join()

        event.accept()