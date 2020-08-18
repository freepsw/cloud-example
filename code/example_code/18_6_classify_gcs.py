from google.cloud import language_v1
from google.cloud.language_v1 import enums, types

# Natural Languae API 인스턴스를 생성합니다.
client = language_v1.LanguageServiceClient()

# 위하고 다르게 gcs_content_uri 파라미터에 GCS URI를 입력합니다.
document = types.module.Document(gcs_content_uri="gs://document-byjw/UptownFunk.txt", type=enums.Document.Type.PLAIN_TEXT)

# classify_text()에 위에서 만든 document를 넣어서 호출합니다.
categories = client.classify_text(document)

print(categories)