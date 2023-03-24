words = ['class', 'function', 'method']
byte_words = [bytes(word, 'utf-8') for word in words]

for byte_word in byte_words:
    print(type(byte_word), byte_word, len(byte_word))
