from google.cloud import pubsub_v1

project_id = 'gcloud-book-byjw'  # GCP 프로젝트 아이디
topic_name = 'test_topic'        # Topic 아이디

# Publisher용 인스턴스 생성
publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/{project_id}/topics/{topic}'.format(
    project_id=project_id,  # 프로젝트 ID 설정
    topic=topic_name        # Topic Name 설정
)

for i in range(10):
    msg = '{index} - Hello World'.format(index=i).encode('utf-8')

    # 위에서 만들어지는 msg를 Topic 에 게시
    publisher.publish(topic=topic_path, data=msg)
