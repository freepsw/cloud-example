from google.cloud import pubsub_v1

project_id = 'gcloud-book-byjw'          # GCP 프로젝트 아이디
topic_name = 'test_topic'                # Topic 아이디
subscription_id = 'test_subscription'  # Subscription 아이디

# Subscriber용 인스턴스 생성
subscriber = pubsub_v1.SubscriberClient()

# topic 경로 생성
# URI 형태 : "projects/gcloud-book-byjw/topics/test_topic"
topic_path = 'projects/{project_id}/topics/{topic}'.format(
    project_id=project_id,
    topic=topic_name
)

# Subscription 경로 생성
# URI 형태 : "projects/gcloud-book-byjw/subscriptions/test_subscription"
subscription_path = 'projects/{project_id}/subscriptions/{subscription_id}'.format(
    project_id=project_id,
    subscription_id=subscription_id
)

def callback(message):
    print(message.data)
    message.ack()

subscribe = subscriber.subscribe(subscription_path, callback)

try:
    subscribe.result()
except Exception as e:
    subscribe.cancel()
