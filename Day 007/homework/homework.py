def binary_to_decimal(binary):
    return int(binary, 2)


def decimal_to_char(decimal):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?.!,’"
    index = decimal - 1
    return alphabet[index] if 0 <= len(alphabet) else ""


def convert_binary_sentence(sentence):
    words = sentence.split("    ")
    converted_words = []

    for i in words:
        letters = i.split(".")
        decode_word = "".join(decimal_to_char(binary_to_decimal(letter)) for letter in letters)
        converted_words.append(decode_word)


    return " ".join(converted_words)


print(convert_binary_sentence("11101.1.1110    11001.1111.10101    10010.101.1.100    10100.1000.1001.10011.110101"))