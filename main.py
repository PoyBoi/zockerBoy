from src.main_stem import (get_color_palette, get_overlay_box, object_detection)
from src.logo_det import run_det
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-img_path', '--i', '-I', type=str, nargs='?', help='Location of the image to be scanned', const=r"image\test_ad.jpg")
parser.add_argument('-dev', '--d', '-D', type=int, choices=[0, 1, 2], help='This changes usage, 0 for cpu, 1 for cuda, 2 for multi-GPU(not built yet)')

args = parser.parse_args()

isAd = 3 # Will change to 4 once logo is added
# img_path = r'C:\\Users\\parvs\\Downloads\\games_cyberpunk_posters.webp'
# device = 1
img_path = args.i 
device = args.d

getPalette = get_color_palette(img_path)
if getPalette == [] or getPalette == None:
    None
else:
    isAd -= 1
textOCR = get_overlay_box(img_path)
if textOCR == "" or textOCR == " " or textOCR == None:
    None
else:
    isAd -= 1
objDetection = run_det(img_path, device)
if objDetection == None:
    None
else:
    isAd -= 1

if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Unix-like systems (macOS, Linux)
    os.system('clear') 

print(
    """
    Color pallete is: {},
    Overlayed text says: {},
    Objects detected are: {}
    """.format(getPalette, textOCR, objDetection)
)

if isAd == 0:
    print("Yes, this is an ad creative.")
else:
    print("No, I don't think this is an ad creative.")