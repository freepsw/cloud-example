import io
from google.cloud import vision_v1p3beta1 as vision


client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/landmark.png', 'rb').read()
image = vision.types.Image(content=content)

response = client.landmark_detection(image=image)
landmarks = response.landmark_annotations

for landmark in landmarks:
    print(landmark)
