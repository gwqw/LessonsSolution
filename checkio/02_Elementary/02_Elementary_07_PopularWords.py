def popular_words(text, words):
    # create res dic
    res_dic = {}
    for w in words:
        res_dic[w] = 0
    # text to lowercase    
    text = text.lower()
    # find words
    cur_word = ''
    for ch in text:
        if not ch in ('., \n\t!'):
            cur_word += ch
        else:
            if cur_word in res_dic:
                res_dic[cur_word] += 1
            cur_word = ''
    return res_dic


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
