# -*- coding: utf-8 -*- 
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# 구문분석을 위한 text
content = '''When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the 
bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, 
and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop 
publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in 
paperback form, 35 years before Google came along: It was idealistic, and overflowing with neat tools and great 
notions. '''

client = language.LanguageServiceClient()

# content에 분석을 위한 text를 넣습니다.
document = {'type': enums.Document.Type.PLAIN_TEXT, 'content': content}
entities = client.analyze_entities(document)

print(entities)