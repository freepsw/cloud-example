import io
from google.cloud import vision_v1p3beta1 as vision

client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/web_detection.jpeg', 'rb').read()
image = vision.types.Image(content=content)

response = client.web_detection(image=image)

print(response)