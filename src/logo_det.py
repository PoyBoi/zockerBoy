from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

if __name__ == '__main__':
    # Use the model
    results = model.train(data="coco128.yaml", epochs=3, device=0, verbose=True)  # train the model
    # results = model.val()  # evaluate model performance on the validation set
    print("Here")
    # results = model(r"C:\Users\parvs\Downloads\bus.jpg", device=0)  # predict on an image
    print("Here again")
    # success = YOLO("yolov8n.pt").export(format="onnx")  # export a model to ONNX format