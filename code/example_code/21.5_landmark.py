# -*- coding: utf-8 -*- 
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


client = vision.ImageAnnotatorClient()

content = io.open('./Experience-Seoul_landmarks_Heunginjimun-Gate_Dongdaemun.jpg', 'rb').read()
image = vision.types.Image(content=content)

response = client.landmark_detection(image=image)
landmarks = response.landmark_annotations

for landmark in landmarks:
    print(landmark)
