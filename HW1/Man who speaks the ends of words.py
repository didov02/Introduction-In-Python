def checkWord(characters, length, orderedFrom):
    actualSize=int(length/3)

    if length % 3 == 2 :
        actualSize=int(length/3 + 1)         
            
    if orderedFrom == "beginning" :
        return characters[0:actualSize]
    elif orderedFrom == "middle" :
        return characters[actualSize:-actualSize]
    elif orderedFrom == "end" :
        return characters[-actualSize:]


def beginning(word) :
    word_size = len(word)

    characters = list(word)
    begin = checkWord(characters, word_size, "beginning")
    result=''.join(begin)

    return result


def middle(word) :
    word_size = len(word)

    characters = list(word)
    mid = checkWord(characters, word_size, "middle")
    result=''.join(mid)

    return result


def end(word):
    word_size = len(word)

    characters = list(word)
    ending = checkWord(characters, word_size, "end")
    result=''.join(ending)

    return result


def split_sentence(sentence):
    words = sentence.split()
    result = []

    for i in range(0,len(words)) :
        currentWord = []

        currentWord.append(beginning(words[i]))
        currentWord.append(middle(words[i]))
        currentWord.append(end(words[i]))

        myTuple = tuple(currentWord)

        result.append(myTuple)

    return result