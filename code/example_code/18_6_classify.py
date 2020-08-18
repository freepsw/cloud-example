from google.cloud import language_v1
from google.cloud.language_v1 import enums

# Natural Language API를 위한 인스턴스
client = language_v1.LanguageServiceClient()

content = '''When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the 
bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, 
and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop 
publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in 
paperback form, 35 years before Google came along: It was idealistic, and overflowing with neat tools and great 
notions. '''

# 분석하고자 하는 위의 문장을 이용하여 document로 만듭니다.
document = {'type': enums.Document.Type.PLAIN_TEXT, 'content': content}

# classify_text()에 위에서 생성한 document를 넣어서 호출하면 결과를 볼 수 있습니다.
categories = client.classify_text(document)

print(categories)