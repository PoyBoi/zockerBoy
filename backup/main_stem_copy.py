# from PIL import Image

# def get_color_counts(path):
#   try:
#     img = Image.open(path)
#     w, h = img.size
#     color_counts = {}
#     for x in range(w):
#       for y in range(h):
#         pixel = img.getpixel((x, y))
#         if pixel in color_counts:
#           color_counts[pixel] += 1
#         else:
#           color_counts[pixel] = 1
#     return color_counts
#   except Exception as e:
#     print(f"Error processing image: {e}")

# def img_resize(path, size):
#     out_path = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\test." + image_path.split(".")[-1]
#     try:
#         img = Image.open(path).resize((size, size))
#         img.save(out_path)
#         return out_path
#     except Exception as e:
#        print("Error reszing image", e)

# Example usage
image_path = r"C:\Users\parvs\OneDrive\Pictures\Cyberpunk 2077\photomode_01032023_011806.png"
# new_path = img_resize(image_path, 10)
# dictN = get_color_counts(new_path)

# print(dictN)
from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief(image_path)

palette = ct.get_palette(color_count=5)
print(palette)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()