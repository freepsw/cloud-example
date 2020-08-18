# -*- coding: utf-8 -*- 
from google.cloud import translate_v2 as translate

client = translate.Client()

text = 'Cloud Translation API에 번역을 요청하면 기본적으로 인공신경망 기계 번역(NMT) 모델을 사용하여 텍스트가 번역됩니다. 요청한 번역 언어 조합에 NMT 모델이 지원되지 않는 ' \
       '경우에는 구문 기반 기계 번역(PBMT) 모델이 사용됩니다.'

result = client.translate(text, target_language='es')

print (result)

# print('원본 텍스트: {input_text}'.format(input_text=result['input']))
# print('번역 텍스트: {translate_text}'.format(translate_text=result['translatedText']))
# print('감지 언어 코드: {detect_language}'.format(detect_language=result['detectedSourceLanguage']))
