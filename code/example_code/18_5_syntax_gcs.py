from google.cloud import language_v1
from google.cloud.language_v1 import enums, types

# Natural Languae API를 위한 인스턴스를 생성합니다.
client = language_v1.LanguageServiceClient()

# Document 부분에 있는 gcs_content_uri 부분에 GCS URI를 넣습니다.
document = types.module.Document(gcs_content_uri="gs://document-byjw/UptownFunk.txt", type=enums.Document.Type.PLAIN_TEXT)

# 위에서 생성한 document를 analyze_syntax에 넣어주면 분석 결과를 확인할 수 있습니다.
tokens = client.analyze_syntax(document)
print(tokens)
