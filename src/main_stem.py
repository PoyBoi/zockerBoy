import matplotlib.pyplot as plt

# image_path = r"C:\Users\parvs\OneDrive\Pictures\Cyberpunk 2077\photomode_01032023_011806.png"

def get_color_palette(img_path = r"zockerBoy\image\test_ad.jpg"):
  try:
    from colorthief import ColorThief
    ct = ColorThief(img_path)

    palette = ct.get_palette(color_count=5)
    plt.imshow([[palette[i] for i in range(5)]])
    plt.show()

    return palette
  except Exception as e:
    print("Encountered error {} in construction of color palette".format(e))

#__main__
# print(get_color_palette(image_path))
    
def get_text_overlay(img_path = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg"):
  from PIL import Image
  import pytesseract

  # Open the image file
  img = Image.open(img_path)
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  #!TODO need to find the tesseract location and then assign it to this variable
  # Use pytesseract to convert the image into text
  text = pytesseract.image_to_string(img)
  return text

#__main__
print(get_text_overlay())