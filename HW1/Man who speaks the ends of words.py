def beginning(word) :
    word_length = len(word)
    size = int(word_length/3)

    if word_length % 3 == 2:
        size = int(word_length/3 + 1)

    result = ''.join(word[0:size])

    return result


def middle(word) :
    word_length = len(word)
    size = int(word_length/3)

    if word_length % 3 == 2:
       size = int(word_length/3 + 1)

    result = ''.join(word[size:-size])

    return result


def end(word):
    word_length = len(word)
    size = int(word_length/3)

    if word_length % 3 == 2:
        size = int(word_length/3 + 1)

    result = ''.join(word[-size:])

    return result


def split_sentence(sentence):
    words = sentence.split()
    result = []

    for word in words :
       my_tuple = beginning(word),middle(word),end(word)
       result.append(my_tuple)

    return result