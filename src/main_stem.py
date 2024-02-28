# ==============================
# For the OCR
import cv2
import pytesseract
from PIL import Image
from pytesseract import Output

# ===============================
# For basic output plotting
import matplotlib.pyplot as plt

# ===============================
# For color palette
from colorthief import ColorThief

# ===============================
# For running moondream (deprecated)
from transformers import AutoModelForCausalLM, CodeGenTokenizerFast as Tokenizer

# ===============================
# For running mmDetection
import mmdet
from mmdet.apis import DetInferencer
# https://pytorch.org/get-started/locally/

# ===============================
# For running Object Detection and logo detection
import io
import subprocess
import argparse
from ultralytics import YOLO
from contextlib import redirect_stdout


# from rudimentary_func import download_file

def get_color_palette(img_path:str = r"zockerBoy\image\test_ad.jpg") -> list:
  try:    
    ct = ColorThief(img_path)

    palette = ct.get_palette(color_count=5)
    plt.imshow([[palette[i] for i in range(5)]])
    plt.show()

    return palette
  except Exception as e:
    print("Encountered error {} in construction of color palette".format(e))
    
def get_text_overlay(img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg") -> str:
  # I could have used CNN's here but that wouldn't be that good compared to this
  # Open the image file
  img = Image.open(img_path)
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  #!TODO Need a way to install tesseract.exe which is automatic
  text = pytesseract.image_to_string(img)
  processed_text = text.split()
  return text

def get_overlay_box(img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg") -> str:
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

  myconfig = r"--psm 6 --oem 3"

  # text_ext = pytesseract.image_to_string(Image.open(img_path), config=myconfig)
  img_box = cv2.imread(img_path)
  # h, w, _ = img_box.shape
  gray_image = cv2.cvtColor(img_box, cv2.COLOR_BGR2GRAY)

  # ret, bw_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  # img_box = bw_image
  
  img_box = gray_image
  out_txt = ""
  data = pytesseract.image_to_data(img_box, config=myconfig, output_type=Output.DICT)
  for i in range(len(data['text'])):
    # Need to find threshold value that gets all of the words but leaves out the stupid one worders
    # might need to apply RE over here, todo for later
    if float(data['conf'][i]) > 75:
      # print(data['text'][i])
      x = data['text'][i]
      ignore_var = ["|"]
      if x not in ignore_var:
        out_txt += x + " "
  # print(out_txt)
  return out_txt

def obj_det(qst:str, img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg") -> str:
  # can use YOLO or moondream and maybe layer it with openCV
  # This does not work because vit_so400m_14_siglip_384 does not want to work

  model_id = "vikhyatk/moondream1"
  model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
  tokenizer = Tokenizer.from_pretrained(model_id)

  img = Image.open(img_path)
  enc_image = model.encode_image(img)
  print(model.answer_question(enc_image, qst, tokenizer))

def object_detection(img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg") -> str:
  inferencer = DetInferencer('rtmdet_tiny_8xb32-300e_coco', device="cuda:0")

  # Perform inference
  inferencer(img_path, 
            show=True,
            pred_score_thr=0.4, 
            # texts= "what in this image can be sold",
            )

# names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}

# if __name__ == '__main__':    
#     def run_det(img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg", dev:int = 0) -> str:
#         model = YOLO("yolov8m.yaml")  # build a new model from scratch
#         model = YOLO(r"zockerBoy\models\yolov8m.pt")  # load a pretrained model (recommended for training)
#         output = []
#         # Use the model
#         # results = model.train(data="coco128.yaml", epochs=3, device=0, verbose=True)  # train the model
#         # results = model.val()  # evaluate model performance on the validation set
#         ## dev == 0 -> CPU, dev == 1 -> GPU if any
#         try:
#             if dev == 0:
#                 results = model(img_path, device="cpu", verbose = True)  # predict on an image
#             elif dev == 1:
#                 results = model(img_path, device="cuda", verbose = True, save_dir = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy")
#             elif dev == 2:
#                 print("Multi GPU not supported yet")
#             else:
#                 print("Incorrect number specified")
#         except Exception as e:
#             print("No CUDA device found. ", e)
        
#         for i in results:
#             boxes = i.boxes
#             # print(boxes.conf)
#             for i in boxes.cls:
#                 op = str(i).split("(")[1].split(".")[0]
#                 output.append(names[int(op)])

#         return output

#__main__

# print(get_color_palette(r"zockerBoy\image\test_ad.jpg"))
# print(get_text_overlay(r"zockerBoy\image\test_ad.jpg"))
# print(get_text_overlay(r"C:\Users\parvs\Downloads\Fwaut2PaEAQynD4.jpg"))
# get_overlay_box(r"C:\Users\parvs\Downloads\Fwaut2PaEAQynD4.jpg")
# obj_det("What is the object in the image ?")
# object_detection(r"C:\Users\parvs\Downloads\WhatsApp Image 2024-02-22 at 00.29.09_30f01e74.jpg")
# print(run_det(r'C:\\Users\\parvs\\Downloads\\games_cyberpunk_posters.webp', 1))