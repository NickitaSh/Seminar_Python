words = ['атрибут', 'class', 'function', 'type']


for word in words:
    try:

        b = bytes(word, 'ascii')
        print(f'{word}  can be written in byte type with b'' marking')
    except:
        print(f'{word} cannot be written in byte type with b'' marking')
