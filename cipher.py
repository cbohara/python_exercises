def solution(word, cipher):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(cipher) != len(alphabet):
        return ''
    for char in cipher:
        if char not in alphabet:
            return ''
    for char in word:
        if char not in alphabet:
            return ''

    mapping = dict()
    for index, cipher_char in enumerate(cipher):
        alpha_char_key = alphabet[index]
        cipher_char_value = cipher[index]
        mapping[alpha_char_key] = cipher_char_value

    output_string = ''
    for char in word:
        output_string += mapping[char]
    return output_string


word = 'helloworld'
cipher = 'mpgzkeyrsxfwlvjbcnuidhoqat'
output = 'rkwwjojnwz'
print(solution(word, cipher))