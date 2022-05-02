from google.cloud import vision
from PIL import Image
import cv2
import numpy as np
import os
import pyautogui

image = pyautogui.screenshot(region=(1700, 100, 200, 50))
image.save(r'C:\Users\JL FRANCISCO\Desktop\user.jpg')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\Downloads\chromatic-trees-342514-99b2f35a2213.json'
img = np.asarray(Image.open('C://Users//JL FRANCISCO//Desktop//user.jpg'))
success, encoded_image = cv2.imencode('.jpg', img)
roi_image = encoded_image.tobytes()
client = vision.ImageAnnotatorClient()
image = vision.Image(content=roi_image)
response = client.text_detection(image=image)
texts = response.text_annotations
result = texts[0].description.strip()
print(result)