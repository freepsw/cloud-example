# -*- coding: utf-8 -*- 
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

content = io.open('./1200px-SK_logo.svg.png', 'rb').read()
image = vision.types.Image(content=content)

response = client.logo_detection(image=image)
logos = response.logo_annotations

for logo in logos:
    print(logo)