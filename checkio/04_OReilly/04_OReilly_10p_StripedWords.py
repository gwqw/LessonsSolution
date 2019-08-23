VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def isword(w):
    # length checking
    if len(w) < 2:
        return False
    
    # check first symbol
    w = w.upper()
    if w[0] in VOWELS:
        isVowel = True
    elif w[0] in CONSONANTS:
        isVowel = False
    else:
        return False
        
    # check other symbols
    for l in w[1:]:
        if l not in VOWELS and l not in CONSONANTS:
            return False
        if l in VOWELS and isVowel:
            return False
        if l in CONSONANTS and not isVowel:
            return False
        isVowel = not isVowel
        
    return True        

def checkio(text):
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.replace('?', ' ')
    text = text.replace('!', ' ')
    words = sum(map(isword, text.split()))
    #words = [w for w in text.split() if isword(w)]
    print(words)
    #return len(words)
    return words

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("To take a trivial example, which of us ever undertakes" + 
                   "laborious physical exercise, except to obtain some advantage" +
                   "from it?") == 8, ""
