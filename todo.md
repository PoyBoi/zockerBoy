# SRC

## main_stem.py

### get_text_overlay()

1. Need to find a way to get PyTesseract to install automatically through a bash file and not have to go through the installation loop
2. Keras_ocr is also a good alternative, will need to check on it later on

### get_overlay_box()

1. Need to find a good way to understand what threshold is good, might need to go a little more DL/CNN route
2. Might need to apply RE to check what the text has to give in totality while also removing the bad reads from the image
3. "--psm 6" feels right for now, can try the other ones, namely 11, 12 to see what else I can improve on the reading
4. Need to add black and white filter and see output differential

# Misc
## Changes made in code
### format: file_name - line of original code
1. vision_encoder.py - line 100
2. vision_encoder.py - line 40