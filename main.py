from zockerBoy.src.main_stem import (get_color_palette, get_overlay_box, object_detection)
from zockerBoy.src.logo_det import run_det
import os

isAd = 3 # Will change to 4 once logo is added
img_path = r'C:\\Users\\parvs\\Downloads\\games_cyberpunk_posters.webp'

getPalette = get_color_palette(img_path)
textOCR = get_overlay_box(img_path)
objDetection = run_det(img_path, 1)

if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Unix-like systems (macOS, Linux)
    os.system('clear') 

print(
    "Color pallete is: {}, \n Overlayed text says: {}, \n Objects detected are: {}".format(getPalette, textOCR, objDetection)
)