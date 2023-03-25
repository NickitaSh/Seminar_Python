# Создаем список слов для преобразования в буквенный формат
words = ['разработка', 'сокет', 'декоратор']

letter_list = []

for word in words:
    letter_word = ''
    for letter in word:
        letter_word += '\\' + format(ord(letter), 'x')
    letter_list.append(letter_word)

for letter_word in letter_list:
    print(type(letter_word), letter_word, len(letter_word))

unicode_list = []
for letter_word in letter_list:
    unicode_word = ''
    for letter in letter_word.split('\\')[1:]:
        unicode_word += chr(int(letter, 16))
    unicode_list.append(unicode_word)

for unicode_word in unicode_list:
    print(type(unicode_word), unicode_word, len(unicode_word))
