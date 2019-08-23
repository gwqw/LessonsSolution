def get_unique_word(line, position):
    word = ""
    for i in line[position:]:
        if not i in word:
            word += i
        else:
            break
    return word

def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    long_word = ""
    for i in range(0,len(line)):
        word = get_unique_word(line, i)
        #print("i = %d, word = %s, long_word = %s" % (i, word, long_word))
        if len(word) > len(long_word):
            long_word = word
    #print(long_word)
    return long_word

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
