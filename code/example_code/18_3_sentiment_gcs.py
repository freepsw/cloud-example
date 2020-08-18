from google.cloud import language_v1
from google.cloud.language_v1 import enums, types

# Natural Language를 위한 인스턴스를 생성합니다.
client = language_v1.LanguageServiceClient()

#  Document를 생성하는데 이번에는 gcs_content_uri 부분에 GCS URI를 넣어서 생성을 합니다.
document = types.module.Document(gcs_content_uri="gs://document-byjw/UptownFunk.txt", type=enums.Document.Type.PLAIN_TEXT)

# analyze_sentiment()에 위에서 생성한 document를 넣어서 호출하면 해당 감정분석 결과를 얻을 수 있습니다.
response = client.analyze_sentiment(document=document)

print(response)

