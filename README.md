# Scripts for cloud examples  

## 1. Run the http load test using hey tool (on ubuntu)
- https://github.com/rakyll/hey
```
sudo apt update
sudo apt install snapd
sudo snap install hey    
hey -z 20s -c 10 -n 1000 http://34.120.78.148
```


## 2. BigQuery Sample data
- https://github.com/datasets/house-prices-uk/blob/master/data/data.csv

```
Date	    Price (All)	Change (All)	Price (New)	Change (New)	Price (Modern)	Change (Modern)	Price (Older)	Change (Older)
1952-11-01	1891	    0.0	            2107	    0.0	2020	0.0	1524	0.0
1953-02-01	1891	    0.0	            2107	    0.0	2002	0.0	1542	0.0
1953-05-01	1891	    0.0	            2107	    0.0	2002	0.0	1542	0.0
1953-08-01	1881	    0.0	            2117	    0.0	2002	0.0	1524	0.0
```

### Query 
```sql
select primary_type , count(primary_type)
from bigquery-public-data.austin_crime.crime
group by primary_type
```

## 3. Google Cloud SDK 설치 (on CentOS 7)
- https://cloud.google.com/sdk/docs/downloads-yum?hl=ko

```
> sudo yum install -y dnf

> sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-cli]
name=Google Cloud CLI
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el8-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

> sudo yum install google-cloud-sdk

> gcloud --version
Google Cloud SDK 305.0.0
alpha 2020.08.07
beta 2020.08.07
bq 2.0.58
core 2020.08.07
gsutil 4.52
kubectl 1.15.11

> gcloud init 


```



### Test gcloud command 
```
> gcloud config set account "freepsw.05@gmail.com"

> gcloud compute instances list
NAME               ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP   STATUS
gcloud-sdk-client  us-central1-a  n1-standard-1               10.128.0.10  34.69.189.78  RUNNING
```


## 4. Cloud Translate API 활용
```
> sudo yum install -y python3-virtualenv
> python3 -m venv sandbox
> source sandbox/bin/activate
> pip install --upgrade pip
> pip install google-cloud-translate
> pip install --upgrade google-cloud-translate
```

### Git code 다운로드 
```
> sudo yum install -y git
> git clone https://github.com/freepsw/cloud-example.git
```

### Cloud Translate API 코드 실행
- service account key 설정
  - 다운 받은 서비스 계정 key 파일을 서버로 전달한 후
  - 아래와 같이 환경설정에 추가 
```
> export GOOGLE_APPLICATION_CREDENTIALS="/home/.../myproject-f4f4ad4248b0.json"
```

- python code 작성
```python
from google.cloud import translate_v2 as translate

client = translate.Client()
result = client.translate('hello', target_language='ja')
print(result['translatedText'])
```

- run python 
```
##  영어 >> 일본어 번역 
> cd ~
> python ~/cloud-example/code/translate_api.py
こんにちは

## 어느 나라 언어인지 판단
> cd ~
> python cloud-example/code/example_code/17_detect.py 
[{'confidence': 1, 'language': 'ko', 'input': '안녕하세요. GCP 입니다.'}]


## 번역을 지원하는 언어 목록 제공 
> python cloud-example/code/example_code/17_get.py
{'language': 'af', 'name': 'Afrikaans'}
{'language': 'ak', 'name': 'Akan'}
{'language': 'sq', 'name': 'Albanian'}
{'language': 'am', 'name': 'Amharic'}
{'language': 'ar', 'name': 'Arabic'}
{'language': 'hy', 'name': 'Armenian'}
{'language': 'as', 'name': 'Assamese'}
{'language': 'ay', 'name': 'Aymara'}
{'language': 'az', 'name': 'Azerbaijani'}
....

## 영어 문장을 한국어로 번역 
> python cloud-example/code/example_code/17_translate.py 
{'translatedText': 'Cuando solicita una traducción de la API de Cloud Translation, el texto se traduce mediante un modelo de traducción automática neuronal artificial (NMT) de forma predeterminada. Si el modelo NMT no es compatible con la combinación de idiomas de traducción solicitada, se utiliza el modelo de traducción automática basada en frases (PBMT).', 'detectedSourceLanguage': 'ko', 'input': 'Cloud Translation API에 번역을 요청하면 기본적으로 인공신경망 기계 번역(NMT) 모델을 사용하여 텍스트가 번역됩니다. 요청한 번역 언어 조합에 NMT 모델이 지원되지 않는 경우에는 구문 기반 기계 번역(PBMT) 모델이 사용됩니다.'}
```


## 5. Cloud Natural Language API 사용 
```
> pip install google-cloud-language
> python cloud-example/code/example_code/18_basic.py 
Text: Hello, world!
Sentiment: 0.600000023842, 0.600000023842

## 문장에서 앤터티 추출 
> gcloud ml language \
    analyze-entities \
    --content="Michelangelo \
    Caravaggio, Italian painter, \
    is known for \
    'The Calling of Saint Matthew' \
    ."

{
  "entities": [
    {
      "mentions": [
        {
          "text": {
            "beginOffset": 0,
            "content": "Michelangelo     Caravaggio"
          },
          "type": "PROPER"
        },
        {
          "text": {
            "beginOffset": 37,
            "content": "painter"
          },
          "type": "COMMON"
        }
      ],
      "metadata": {
        "mid": "/m/020bg",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Caravaggio"
      },
      "name": "Michelangelo Caravaggio",
      "salience": 0.82904786,
      "type": "PERSON"
    },
    {
      "mentions": [
        {
          "text": {
            "beginOffset": 29,
            "content": "Italian"
          },
          "type": "PROPER"
        }
      ],
      "metadata": {},
      "name": "Italian",
      "salience": 0.13981608,
      "type": "LOCATION"
    },
    {
      "mentions": [
        {
          "text": {
            "beginOffset": 68,
            "content": "The Calling of Saint Matthew"
          },
          "type": "PROPER"
        }
      ],
      "metadata": {
        "mid": "/m/085_p7",
        "wikipedia_url": "https://en.wikipedia.org/wiki/The_Calling_of_St_Matthew"
      },
      "name": "The Calling of Saint Matthew",
      "salience": 0.031136045,
      "type": "EVENT"
    }
  ],
  "language": "en"
}
```

## 6. Vision API 사용 
```
> cd cloud-example/code/example_code
> sudo yum install -y wget 
> wget https://news.kbs.co.kr/data/news/2020/08/18/4519442_lI7.jpg

> pip install google-cloud-vision

# 이미지에서 문자열의 위치와 문자열을 추출한다.
# https://cloud.google.com/vision/docs/fulltext-annotations?hl=ko  
> python cloud-example/code/example_code/21.2_document.py
Block confidence: 0.990000009537

Paragraph confidence: 0.990000009537
Word text: JAYS (confidence: 0.990000009537)
        Symbol: J (confidence: 0.990000009537)
        Symbol: A (confidence: 0.990000009537)
        Symbol: Y (confidence: 0.990000009537)
        Symbol: S (confidence: 0.990000009537)

Block confidence: 0.990000009537

Paragraph confidence: 0.990000009537
Word text: UE (confidence: 0.990000009537)
        Symbol: U (confidence: 0.990000009537)
        Symbol: E (confidence: 0.990000009537)


# 지역별로 중요한 랜드마크 이름을 추출한다. 
<!-- > wget https://www.agoda.com/wp-content/uploads/2018/10/Experience-Seoul_landmarks_Heunginjimun-Gate_Dongdaemun.jpg -->
> wget https://cdn.britannica.com/83/99583-050-792F1327/Eiffel-Tower-Paris.jpg
> python cloud-example/code/example_code/21.5_landmark.py 
mid: "/m/03hvjr"
description: "Heunginjimun"
score: 0.785608172417

# 유명한 회사/브랜드의 로고를 추출한다.
> wget https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/SK_logo.svg/1200px-SK_logo.svg.png
> python cloud-example/code/example_code/21.7_logo.py 
mid: "/m/04dj27"
description: "SK Group"
score: 0.994797587395

# Extract the text from image
> wget https://image-en.bespinglobal.com/wp-content/uploads/2018/06/google-cloud-platform.jpg
> python cloud-example/code/example_code/21.8_ocr.py 
Google Cloud Platform

Block confidence: 0.0

Paragraph confidence: 0.0
Word text: Google (confidence: 0.0)
        Symbol: G (confidence: 0.0)
        Symbol: o (confidence: 0.0)
        Symbol: o (confidence: 0.0)
        Symbol: g (confidence: 0.0)
        Symbol: l (confidence: 0.0)
        Symbol: e (confidence: 0.0)
Word text: Cloud (confidence: 0.0)
        Symbol: C (confidence: 0.0)
        Symbol: l (confidence: 0.0)
        Symbol: o (confidence: 0.0)
        Symbol: u (confidence: 0.0)
        Symbol: d (confidence: 0.0)
Word text: Platform (confidence: 0.0)
        Symbol: P (confidence: 0.0)
        Symbol: l (confidence: 0.0)
        Symbol: a (confidence: 0.0)
        Symbol: t (confidence: 0.0)
        Symbol: f (confidence: 0.0)
        Symbol: o (confidence: 0.0)
        Symbol: r (confidence: 0.0)
        Symbol: m (confidence: 0.0)
```


## 7. Cloud Function + Vision API + BigQuery 

```
> cd cloud-example/code/example_code
> wget https://image-en.bespinglobal.com/wp-content/uploads/2018/06/google-cloud-platform.jpg
```

- cloud function 
``` python
# -*- coding: utf-8 -*- 
import io
import os
from google.cloud import vision
# from google.cloud.vision import types

from google.cloud import bigquery

def detect_text(event, context):
    vision_client = vision.ImageAnnotatorClient()
    bigquery_client = bigquery.Client()

    # GCS 이벤트로부터 전달 받은 버킷 이름과 네임을 이용하여 GCS URI 만드는 부분
    bucket_uri = 'gs://{bucket}/{file}'.format(bucket=event['bucket'], file=event['name'])

    # Vision API에 GCS URI를 넘겨서 TEXT 추출하여 가져오기
    response = vision_client.text_detection({'source': {'image_uri': bucket_uri}}).full_text_annotation.text

    # 위에서 얻은 GCS URI와 텍스트를 빅쿼리에 넣어주는 쿼리 작성
    # projct-id는 본인의 project id로 변경한다. 
    query = """insert into `project-id.function_dataset.image_text` (image_url, detect_text) values ('{bucket}', '''{text}''');""".format(bucket=bucket_uri, text=response)

    # 위에서 만든 쿼리로 빅쿼리에 실행
    bigquery_client.query(query)

```

- requirements.txt
```     
google-cloud-vision==1.0.0
google-cloud-bigquery==1.27.2
```
- BigQuery SQL 구문
```sql
select * from firm-capsule-256012.function_dataset.image_text
```


## [ETC] 
### Test Code 
- 구글 클라우드 플랫폼 뽀개기 코드 활용
    - https://github.com/bjpublic/googlecloud