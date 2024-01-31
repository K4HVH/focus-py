import win32api
import time

from mouse_driver.MouseMove import mouse_move
from focus.utils import *

class Control:
    terminate_flag = False
    current_weapon_data = None
    mouse_thread = None
    update_flag = False

    @classmethod
    def drive_mouse(cls):
        if cls.current_weapon_data is None:
            print("No weapon data available.")
            return
        
        max_instructions = len(cls.current_weapon_data)
        complete = False
        print(cls.current_weapon_data)

        while not cls.terminate_flag:
            if cls.update_flag:
                max_instructions = len(cls.current_weapon_data)  # Update max_instructions
                print(f"Updated weapon data: {cls.current_weapon_data}")
                cls.update_flag = False
                continue

            if win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0 and win32api.GetKeyState(0x91) & 1 and complete == False:
                for index, instruction in enumerate(cls.current_weapon_data):
                    x, y, duration = instruction[0], instruction[1], instruction[2]
                    currtime = time.perf_counter()
                    int_timer = 0

                    while int_timer < duration/1000 and win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0 and win32api.GetKeyState(0x91) & 1:
                        int_timer = time.perf_counter() - currtime
                        mouse_move(x, y)

                        #do autofire here
                        Timer.high_precision_sleep(0.01)
                    
                    if index == max_instructions - 1:
                        complete = True
            elif win32api.GetKeyState(0x01) >= 0 or win32api.GetKeyState(0x02) >= 0 or win32api.GetKeyState(0x91) & 0:
                complete = False

    @classmethod
    def stop_mouse(cls):
        cls.terminate_flag = True

    @classmethod
    def start_mouse(cls):
        cls.terminate_flag = False

    @classmethod
    def update_weapon_data(cls, new_weapon_data):
        cls.current_weapon_data = new_weapon_data
        cls.update_flag = True