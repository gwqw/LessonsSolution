"""
    Bird language: after consonant bird adds random vowel
    after vowel bird adds two the same letters
"""

VOWELS = "aeiouy"

def translate(phrase):
    res = ""
    skip = 0
    for letter in phrase:
        if skip:
            skip -= 1
            continue
        if letter in VOWELS:
            res += letter
            skip = 2
        elif letter == ' ':
            res += letter
        else:
            res += letter
            skip = 1            
    return res

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
