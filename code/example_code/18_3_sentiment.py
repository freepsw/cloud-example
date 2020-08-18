# -*- coding: utf-8 -*- 
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Natural Language API를 위한 인턴스를 생성합니다.
client = language.LanguageServiceClient()

content = '''When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the 
bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, 
and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop 
publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in 
paperback form, 35 years before Google came along: It was idealistic, and overflowing with neat tools and great 
notions. '''

# 분석해야할 텍스트를 아래와 같은 형식으로 생성합니다.
document = {'type': enums.Document.Type.PLAIN_TEXT, 'content': content}

# analyze_sentiment() 메서드에 위에서 만든 document를 전달하면 해당 document에 대한 감정분석 결과를 확인할 수 있습니다.
response = client.analyze_sentiment(document=document)

print(response)

