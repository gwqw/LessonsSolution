def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    max_length = 0
    cl = 0
    last_char = ''
    for c in line:
        if c == last_char:
            cl += 1
        else:
            if cl > max_length: max_length = cl
            cl = 1
        last_char = c
    if cl > max_length: max_length = cl
    return max_length

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('aa') == 2, "Third"
    print('"Run" is good. How is "Check"?')
