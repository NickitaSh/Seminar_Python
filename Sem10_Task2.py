words = ['class', 'function', 'method']

byte_list = []

for word in words:
    byte_word = b''
    for letter in word:
        byte_word += bytes([ord(letter)])
    byte_list.append(byte_word)

for byte_word in byte_list:
    print(type(byte_word), byte_word, len(byte_word))
