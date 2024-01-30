import time
import json

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

class Timer:
    def high_precision_sleep(duration):
        start_time = time.perf_counter()
        while True:
            elapsed_time = time.perf_counter() - start_time
            remaining_time = duration - elapsed_time
            if remaining_time <= 0:
                break
            if remaining_time > 0.02:  # Sleep for 5ms if remaining time is greater
                time.sleep(max(remaining_time/2, 0.0001))  # Sleep for the remaining time or minimum sleep interval
            else:
                pass