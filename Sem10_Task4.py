words = ['разработка', 'администрирование', "protocol", "standard"]

byte_repr = []

for word in words:
    byte_repr.append(word.encode())

print(byte_repr)

for byte_word in byte_repr:
    print(byte_word.decode())
