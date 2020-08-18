from google.cloud import translate

# 인스턴스를 만듭니다.
client = translate.Client()

# get_languages()를 이용하면 리스트 형태로 반환이 되기 때문에 for 문으로 출력하겠습니다.
for language in client.get_languages():
    print(language)