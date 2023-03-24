words = ["development", "socket", "decorator"]

sorted_letters = []
for word in words:
    sorted_word = sorted(word)
    sorted_letters.append(sorted_word)

for i, word in enumerate(words):
    print(f"Sorted letters for {word}: {sorted_letters[i]}")
    print(f"Type of sorted letters for {word}: {type(sorted_letters[i])}\n")

code_points = []
for word in words:
    word_code_points = []
    for letter in word:
        word_code_points.append(ord(letter))
    code_points.append(word_code_points)

for i, word in enumerate(words):
    print(f"Code points for {word}: {code_points[i]}")
    print(f"Type of code points for {word}: {type(code_points[i])}\n")
