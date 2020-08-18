import io
from google.cloud import vision_v1p3beta1 as vision

client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/logo.jpg', 'rb').read()
image = vision.types.Image(content=content)

response = client.logo_detection(image=image)
logos = response.logo_annotations

for logo in logos:
    print(logo)