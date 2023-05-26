# -*- coding: utf-8 -*- 
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

client = vision.ImageAnnotatorClient()

content = io.open('./Eiffel-Tower-Paris.jpg', 'rb').read()
image = vision.Image(content=content)

response = client.landmark_detection(image=image)
landmarks = response.landmark_annotations

for landmark in landmarks:
    print(landmark)
