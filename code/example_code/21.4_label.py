import io
from google.cloud import vision_v1p3beta1 as vision

client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/label.jpeg', 'rb').read()
image = vision.types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
    print(label)