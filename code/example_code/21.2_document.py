import io
from google.cloud import vision_v1p3beta1 as vision

# vision api 인스턴스를 생성합니다.
client = vision.ImageAnnotatorClient()

# 분석하고자 하는 그림 파일을 불러옵니다.
content = io.open('/Users/jungwoon/Desktop/document.png', 'rb').read()

# types.Image에 위에서 열어온 그림 파일을 지정합니다.
image = vision.types.Image(content=content)

# document_text_detection을 호출하면 해당 분석 결과를 불러옵니다.
response = client.document_text_detection(image=image)

for page in response.full_text_annotation.pages:
    for block in page.blocks:
        print('\nBlock confidence: {}\n'.format(block.confidence))

        for paragraph in block.paragraphs:
            print('Paragraph confidence: {}'.format(
                paragraph.confidence))

            for word in paragraph.words:
                word_text = ''.join([
                    symbol.text for symbol in word.symbols
                ])
                print('Word text: {} (confidence: {})'.format(
                    word_text, word.confidence))

                for symbol in word.symbols:
                    print('\tSymbol: {} (confidence: {})'.format(
                        symbol.text, symbol.confidence))