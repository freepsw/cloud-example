# -*- coding: utf-8 -*- 
from google.cloud import translate_v2 as translate

client = translate.Client()
results = client.detect_language(['안녕하세요. GCP 입니다.'])

print(results)