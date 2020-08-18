from google.cloud import vision_v1p3beta1 as vision
from google.cloud import bigquery

def detect_text(event, context):
    vision_client = vision.ImageAnnotatorClient()
    bigquery_client = bigquery.Client()

    # GCS 이벤트로부터 전달 받은 버킷 이름과 네임을 이용하여 GCS URI 만드는 부분
    bucket_uri = 'gs://{bucket}/{file}'.format(bucket=event['bucket'], file=event['name'])

    # Vision API에 GCS URI를 넘겨서 TEXT 추출하여 가져오기
    response = vision_client.text_detection({'source': {'image_uri': bucket_uri}}).full_text_annotation.text

    # 위에서 얻은 GCS URI와 텍스트를 빅쿼리에 넣어주는 쿼리 작성
    query = """insert into `snappy-helper-239504.functions.ocr` (image_path, detect_text) values ('{bucket}', '''{text}''');""".format(bucket=bucket_uri, text=response)

    # 위에서 만든 쿼리로 빅쿼리에 실행
    bigquery_client.query(query)
