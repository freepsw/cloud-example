import io
from google.cloud import vision_v1p3beta1 as vision


client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/face.jpg', 'rb').read()
image = vision.types.Image(content=content)


response = client.face_detection(image=image)
faces = response.face_annotations

for face in faces:
    print(face)

