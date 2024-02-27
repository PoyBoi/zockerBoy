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
  print(out_txt)

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



#__main__

# print(get_color_palette(r"zockerBoy\image\test_ad.jpg"))
# print(get_text_overlay(r"zockerBoy\image\test_ad.jpg"))
# print(get_text_overlay(r"C:\Users\parvs\Downloads\Fwaut2PaEAQynD4.jpg"))
# get_overlay_box(r"C:\Users\parvs\Downloads\Fwaut2PaEAQynD4.jpg")
# obj_det("What is the object in the image ?")
object_detection(r"C:\Users\parvs\Downloads\WhatsApp Image 2024-02-22 at 00.29.09_30f01e74.jpg")