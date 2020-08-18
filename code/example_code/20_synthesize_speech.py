from google.cloud import texttospeech

# Text-to-Speech 인스턴스를 생성합니다.
client = texttospeech.TextToSpeechClient()

# 만들고자 하는 텍스트를 SynthesisInput에 넣습니다.
input_text = texttospeech.types.SynthesisInput(text="Hi how are you my name is jungwoon")

# Voice 타입을 설정합니다. 여기서는 영어로 하고 여성의 음성으로 하였습니다.
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

# mp3로 생성하기 위해서 아래와 같이 생성을 합니다.
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# 그 다음 synthesize_speech()에 input_text와 voice 및 audio 설정을 넣어서 결과를 받습니다.
response = client.synthesize_speech(input_text, voice, audio_config)

# 그 다음 'output.mp3'란 파일을 만들어서 위에서 만들어진 음성의 결과를 씁니다.
# 그럼 텍스트로부터 만들어진 음성파일이 생성이 됩니다.
with open('output.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
