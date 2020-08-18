import io
from google.cloud import vision_v1p3beta1 as vision

client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/localize_object.jpeg', 'rb').read()
image = vision.types.Image(content=content)

response = client.object_localization(image=image)

objects = response.localized_object_annotations

for object_ in objects:
    print(object_)