import win32api
import time

from mouse_driver.MouseMove import mouse_move
from focus.utils import *

class Control:
    def drive_mouse(weapon_data):
        max_instructions = len(weapon_data)
        complete = False

        while True:
            if win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0 and win32api.GetKeyState(0x91) & 1 and complete == False:
                for index, instruction in enumerate(weapon_data):
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