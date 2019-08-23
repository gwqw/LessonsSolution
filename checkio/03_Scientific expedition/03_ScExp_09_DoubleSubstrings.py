def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    max_length = 0
    print("")
    print("line= ", line)
    # through all pattern length
    for pattern_length in range(1,len(line) // 2 + 1):
        print("pattern_length= ", pattern_length)
        # through all substrings
        for pos in range(0,len(line)-pattern_length+1):
            print("pos= ", pos)
            subs = line[pos:pos+pattern_length]
            print("substring= ", subs)
            pos2 = line.rfind(subs)
            print("pos2= ", pos2)
            if (pos2 - pos) >= pattern_length:
                max_length = pattern_length
                print(max_length)
                break
            
    return max_length

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    assert double_substring("abababaab") == 3, "aba_aba__"
    print('"Run" is good. How is "Check"?')
