# SRC

## main_stem.py

### get_text_overlay()

1. Need to find a way to get PyTesseract to install automatically through a bash file and not have to go through the installation loop
2. Keras_ocr is also a good alternative, will need to check on it later on

### get_overlay_box()

1. Need to find a good way to understand what threshold is good, might need to go a little more DL/CNN route
2. "--psm 6" feels right for now, can try the other ones, namely 11, 12 to see what else I can improve on the reading
3. ~~Need to add black and white filter and see output differential~~
    1. Need to add thresholding to the filter applied
    2. Need to add output cleaning using re
4. Need to improve quality of text being read

### object_detection()

1. Alternatives for object detection: yoloX, mmDetection, yoloV(4/7/8), openCV, moondream, timm

# Misc
## Changes made in code
### format: file_name - line of original code
1. vision_encoder.py - line 100
2. vision_encoder.py - line 40

## Code that works
1. get_color_palette()
    this gets the color palette from the image and returns the top 5 most 
2. get_overlay_box()
    this turns the image to black and white and then ocr's the image
3. 