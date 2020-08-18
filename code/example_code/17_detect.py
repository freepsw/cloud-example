from google.cloud import translate

client = translate.Client()
results = client.detect_language(['안녕하세요. GCP 입니다.'])

print(results)