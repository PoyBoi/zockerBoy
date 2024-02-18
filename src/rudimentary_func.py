import requests
import cv2
import pytesseract

def download_file(url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe", save_location = "zockerBoy\models"):
  response = requests.get(url, stream=True)
  response.raise_for_status()
  filename = response.headers.get('content-disposition', None)
  if filename:
    filename = filename.split('=')[1].strip('"')
  else:
    filename = url.split('/')[-1]
  save_path = f"{save_location}/{filename}"
  with open(save_path, 'wb') as f:
    for chunk in response.iter_content(1024):
      if chunk:
        f.write(chunk)

  print(f"Downloaded file: {save_path}")

def draw_text_box(img_path, new_path):
  import cv2
  # img = cv2.imread(r"zockerBoy\image\test_ad.jpg")
  img = cv2.imread(img_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  blur = cv2.GaussianBlur(gray,(5,5),0)

  ret, thresh1 = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV) 


  rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) 

  dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 

  contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                  cv2.CHAIN_APPROX_NONE) 

  for cnt in contours: 
      x, y, w, h = cv2.boundingRect(cnt) 
      
      # Drawing a rectangle on copied image 
      rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) 
    
  # cv2.imwrite(r'zockerBoy\image\blinkit_1.jpg', img)
  cv2.imwrite(new_path, img)

def cluster_text_boxes(img_path, cluster_threshold):
  img = cv2.imread(img_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)

  _, thresh1 = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

  rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
  dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

  contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

  clusters = []
  current_cluster = []
  for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Crop the text region
    cropped_img = img[y:y+h, x:x+w]

    # Use Tesseract for OCR (replace with your preferred OCR engine)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(cropped_img, config='--psm 6')

    current_cluster.append((x, y, w, h, text))

    # Check for proximity and start new cluster if needed
    if len(current_cluster) > 1:
      # Calculate average center of current cluster
      center_x = sum(box[0] for box in current_cluster) / len(current_cluster)
      max_dist = max(abs(box[0] - center_x) for box in current_cluster)
      if max_dist > cluster_threshold:
        clusters.append(current_cluster)
        current_cluster = []

  # Add the last cluster (if any)
  if current_cluster:
    clusters.append(current_cluster)

  # Save each cluster as a separate image
  cluster_count = 1
  for cluster in clusters:
    cluster_img = img.copy()
    for box in cluster:
      x, y, w, h, _ = box
      cv2.rectangle(cluster_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(f"cluster_{cluster_count}.jpg", cluster_img)
    cluster_count += 1

# __main__
# draw_text_box(r"zockerBoy\image\test_ad.jpg", r'zockerBoy\image\blinkit_1.jpg')

# This did not work out, thresholding is really bad for openCV
cluster_text_boxes(r"zockerBoy\image\test_ad.jpg", 500)