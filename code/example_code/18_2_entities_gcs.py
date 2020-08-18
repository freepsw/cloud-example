from google.cloud import language_v1
from google.cloud.language_v1 import enums, types

# Natural Language API를 위한 인스턴스 생성
client = language_v1.LanguageServiceClient()

# 이 부분에서 gcs_content_url 부분에 GCS URI를 입력합니다.
document = types.module.Document(gcs_content_uri="gs://document-byjw/UptownFunk.txt", type=enums.Document.Type.PLAIN_TEXT)

# analyze_entities()에 위에서 만들어진 document를 호출합니다.
response = client.analyze_entities(document)

print(response)