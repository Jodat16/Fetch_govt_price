import easyocr

reader = easyocr.Reader(['ur']) # specify the language  
result = reader.readtext('./price_list/page_1.jpg')

for (bbox, text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')