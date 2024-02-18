import matplotlib.pyplot as plt
# from rudimentary_func import download_file

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
    
def get_text_overlay(img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg") -> str:
  from PIL import Image
  import pytesseract
  # I could have used CNN's here but that wouldn't be that good compared to this

  # Open the image file
  img = Image.open(img_path)
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  # Need a way to install tesseract.exez
  text = pytesseract.image_to_string(img)
  return text

#__main__
print(get_text_overlay(r"zockerBoy\image\blinkit.png"))