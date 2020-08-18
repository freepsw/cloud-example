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
> sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
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
> sudo yum -y install python-pip
> sudo pip install --upgrade pip
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
> python code/translate_api.py 
こんにち


> cd cloud-example/code/example_code
> python 17_detect.py 

> python 17_get.py

> python 17_translate.py 
```


## 5. Cloud Natural Language API 사용 
```
> pip install google-cloud-language
> cd cloud-example/code/example_code
> python 18_basic.py 
Text: Hello, world!
Sentiment: 0.600000023842, 0.600000023842
```

## 6. Vision API 사용 
```
> cd cloud-example/code/example_code
> sudo yum install -y wget 
> wget https://news.kbs.co.kr/data/news/2020/08/18/4519442_lI7.jpg

> pip install google-cloud-vision
> python 21.2_document.py
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



> wget https://www.agoda.com/wp-content/uploads/2018/10/Experience-Seoul_landmarks_Heunginjimun-Gate_Dongdaemun.jpg
> python 21.5_landmark.py 
mid: "/m/03hvjr"
description: "Heunginjimun"
score: 0.785608172417


> wget https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/SK_logo.svg/1200px-SK_logo.svg.png
> python 21.7_logo.py 
mid: "/m/04dj27"
description: "SK Group"
score: 0.994797587395
```

## [ETC] 
### Test Code 
- 구글 클라우드 플랫폼 뽀개기 코드 활용
    - https://github.com/bjpublic/googlecloud