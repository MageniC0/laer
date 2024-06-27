import os
import json

class ColorManager:
    def __init__(self, file_path='resources/colors.json'):
        self.file_path = file_path
        with open(file_path, 'r') as f:
            self.colors = json.load(f)

    def get_rgb(self, code):
        if isinstance(code, str):
            for color in self.colors:
                if color['name'] == code:
                    return color['rgb']
            return None
        elif isinstance(code, int):
            for color in self.colors:
                if color['code'] == code:
                    return color['rgb']
            return None
        else:
            return None

    def set_rgb(self, code, rgb):
        if isinstance(code, int):
            for color in self.colors:
                if color['code'] == code:
                    color['rgb'] = rgb
                    break
        elif isinstance(code, str):
            for color in self.colors:
                if color['name'] == code:
                    color['rgb'] = rgb
                    break
        self.save()

    def set_name(self, code, name):
        if isinstance(code, int):
            for color in self.colors:
                if color['code'] == code:
                    color['name'] = name
                    break
        elif isinstance(code, str):
            for color in self.colors:
                if color['name'] == code:
                    color['name'] = name
                    break
        self.save()

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.colors, f, indent=4)

# Example usage:
color_manager = ColorManager()
print(color_manager.get_rgb("A"))  # Get RGB values of "A"
print(color_manager.get_rgb(1))   # Get RGB values of code 1
color_manager.set_rgb("A", [255, 0, 0])  # Set new RGB values for "A"
color_manager.set_name(1, "Red")  # Set new name for code 1
