development = ''.join(sorted('development'))
socket = ''.join(sorted('socket'))
decorator = ''.join(sorted('decorator'))


def get_codepoints(word):
    return {ord(char) for char in word}


development_codepoints = get_codepoints(development)
socket_codepoints = get_codepoints(socket)
decorator_codepoints = get_codepoints(decorator)

print(type(development), development)
print(type(socket), socket)
print(type(decorator), decorator)

print(type(development_codepoints), development_codepoints)
print(type(socket_codepoints), socket_codepoints)
print(type(decorator_codepoints), decorator_codepoints)
