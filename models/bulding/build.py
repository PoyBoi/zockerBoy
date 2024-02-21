import mmdet
from mmdet.apis import DetInferencer
print(mmdet.__version__)

inferencer = DetInferencer('rtmdet_tiny_8xb32-300e_coco')

# Perform inference
inferencer(r"C:\Users\parvs\VSC Codes\Python-root\zockerBoy\image\test_ad.jpg", show=True, )