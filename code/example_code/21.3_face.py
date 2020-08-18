# -*- coding: utf-8 -*- 
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

content = io.open('./4519442_lI7.jpg', 'rb').read()
image = vision.types.Image(content=content)


response = client.face_detection(image=image)
faces = response.face_annotations

for face in faces:
    print(face)

