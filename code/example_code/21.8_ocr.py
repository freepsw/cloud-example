import io
from google.cloud import vision_v1p3beta1 as vision


client = vision.ImageAnnotatorClient()

content = io.open('/Users/jungwoon/Desktop/a.jpeg', 'rb').read()
image = vision.types.Image(content=content)

response = client.text_detection(image=image)

print(response.full_text_annotation.text)

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