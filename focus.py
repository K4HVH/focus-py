from PyQt6.QtWidgets import QApplication

from focus.utils import WeaponData
from focus.menu import Menu
        
def main():

    weapons_path = 'weapons.json'
    weapon_list = WeaponData(weapons_path)

    app = QApplication([])
    menu = Menu(weapon_list)
    menu.show()
    app.exec()
    

if __name__ == "__main__":
    main()