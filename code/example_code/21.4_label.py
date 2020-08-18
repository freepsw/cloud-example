# -*- coding: utf-8 -*- 
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

content = io.open('./4519442_lI7.jpg', 'rb').read()
image = vision.types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
    print(label)