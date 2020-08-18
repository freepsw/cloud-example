from google.cloud import translate_v2 as translate

client = translate.Client()
result = client.translate('hello', target_language='ja')
print(result['translatedText'])