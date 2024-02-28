import io
import subprocess
import argparse
from ultralytics import YOLO
from contextlib import redirect_stdout

# ===============================
# Making the argparse
# ===============================

parser = argparse.ArgumentParser()
parser.add_argument('-img_path', '--i', '-I', type=str, nargs=1, help='Location of the image to be scanned')
parser.add_argument('-dev', '--d', '-D', type=int, choices=[0, 1, 2], help='This changes usage, 0 for cpu, 1 for cuda, 2 for multi-GPU(not built yet)')

args = parser.parse_args()

# ===============================
# Main code
# ===============================

names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}

#if __name__ == '__main__':    
def run_det(img_path:str = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg", dev:int = 0) -> str:
    try:
        model = YOLO("yolov8m.yaml")  # build a new model from scratch
        model = YOLO(r"zockerBoy\models\yolov8m.pt")  # load a pretrained model (recommended for training)
        output = []
        # Use the model
        # results = model.train(data="coco128.yaml", epochs=3, device=0, verbose=True)  # train the model
        # results = model.val()  # evaluate model performance on the validation set
        ## dev == 0 -> CPU, dev == 1 -> GPU if any
        try:
            if dev == 0:
                results = model(img_path, device="cpu", verbose = True)  # predict on an image
            elif dev == 1:
                results = model(img_path, device="cuda", verbose = True, save_dir = r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy")
            elif dev == 2:
                print("Multi GPU not supported yet")
            else:
                print("Incorrect number specified")
        except Exception as e:
            print("No CUDA device found. ", e)
        
        for i in results:
            boxes = i.boxes
            # print(boxes.conf)
            for i in boxes.cls:
                op = str(i).split("(")[1].split(".")[0]
                output.append(names[int(op)])
        # print(output)
        return output
    except Exception as e:
        print("Encountered error ", e)

if args.i == None or args.d == None:
    # print("Incorrect / Not enough variables supplied")
    # print("Loading")
    None
else:
    run_det(args.i, args.d)
            
# run_det(r'C:\\Users\\parvs\\Downloads\\games_cyberpunk_posters.webp', 1)