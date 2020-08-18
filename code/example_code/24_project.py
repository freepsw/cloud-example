import datetime
import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms import window
from google.cloud import language_v1
from google.cloud.language_v1 import enums

project = 'skillful-hull-243913'
topic = 'projects/skillful-hull-243913/topics/twitter'
dataset = 'twitter'
noun_table = 'noun'

pipeline_options = PipelineOptions(
    project=project,  # Project ID
    runner='dataflow',  # GCP Dataflow에서 돌리기 위함
    temp_location='gs://twitter-feed-dataflow-temp/temp/',
    streaming=True
)


# Pub/Sub 으로부터 전달받은 데이터를 파싱해서 Syntax 분석하여 명사만 전달
class TwitterFeedParseAndSyntaxAnalyze(beam.DoFn):
    def process(self, element, *args, **kwargs):
        json_object = json.loads(element.decode('utf-8'))
        text = str(json_object['text'])
        lang = str(json_object['lang'])

        print('text : ', text)
        print('lang : ', lang)

        try:
            client = language_v1.LanguageServiceClient()
            document = {'type': enums.Document.Type.PLAIN_TEXT, 'content': text}
            tokens = client.analyze_syntax(document).tokens

            for token in tokens:
                if token.part_of_speech.tag == 6:  # NOUN
                    word = str(token.text.content)

                    if word != '#' and not word.startswith('http'):
                        print('NOUN :', token.text.content)

                        yield token.text.content
        except Exception as e:
            print('Exception : ', e)

# Timestamp를 추가하여 Dictionary 형태로 만듭니다.
class AddTimestamp(beam.DoFn):
    def process(self, element, *args, **kwargs):
        KST = datetime.timezone(datetime.timedelta(hours=9))
        timestamp = datetime.datetime.now(tz=KST).timestamp()

        yield {'date': timestamp, 'word': element[0], 'count': element[1]}


with beam.Pipeline(options=pipeline_options) as pipeline:
    nl_pipeline = pipeline \
                  | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(topic=topic) \
                  | 'ParseTwitter' >> beam.ParDo(TwitterFeedParseAndSyntaxAnalyze()) \
                  | 'Window' >> beam.WindowInto(window.FixedWindows(30)) \
                  | 'Count' >> beam.combiners.Count.PerElement() \
                  | 'AddTimestamp' >> beam.ParDo(AddTimestamp()) \
                  | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
                        table=noun_table,
                        dataset=dataset,
                        project=project,
                        schema='date:TIMESTAMP, word:STRING, count:INTEGER',
                        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
