import io
from google.cloud import speech
from google.cloud.speech import enums, types

# Speech-to-Text API를 윙한 인스턴스를 생성합니다.
client = speech.SpeechClient()

# mp3로 text로 받을 음성파일을 열어서 content에 담습니다.
audio_file = io.open("output.mp3", 'rb')
content = audio_file.read()

# RecongnitionAudio()에 위에서 생성한 audio file을 전달흡니다.
# audio = types.RecognitionAudio(content=content)
audio = types.RecognitionAudio(uri='gs://sample-audio-byjw/output.mp3')

# 음성 관련 설정도 RecognitionConfig를 통해서 설정합니다.
# 여기서는 인코딩은 LINEAR16으로 하고 sample_rate는 16,000 헤르쯔
# 그리고 언어는 영어로 설정하겠습니다.
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# 그 다음 위에서 만들 설정과 audio를 전달하면 dictation한 텍스트를 받을 수 있습니다.
response = client.recognize(config, audio)

print(response)