from google.cloud import language_v1
from google.cloud.language_v1 import enums, types

# Natural Language API를 위한 인스턴스를 생성합니다.
client = language_v1.LanguageServiceClient()

# Document()에 gcs_content_uri 파라미터에 GCS URI를 넣어서 document를 생성합니다.
document = types.module.Document(gcs_content_uri="gs://document-byjw/UptownFunk.txt", type=enums.Document.Type.PLAIN_TEXT)

# 위에서 생성한 document를 analyze_entity_sentiment() 메서드에 넣어서 호출하면 결과를 받을 수 있습니다.
result = client.analyze_entity_sentiment(document)

print(result)