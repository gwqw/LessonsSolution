def verify_anagrams(first_word, second_word):
    first_word = list(first_word.lower())
    second_word = second_word.lower()
    for l in second_word:
        if l in first_word:
            first_word.remove(l)
        elif l.isspace():
            continue
        else:
            return False
    first_word = ''.join(first_word)
    return len(first_word) == 0 or first_word.isspace()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
