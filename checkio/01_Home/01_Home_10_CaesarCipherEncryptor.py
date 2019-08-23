def encr_letter(l, delta):
    print("letter: ", l)
    i = ord(l) - ord('a')
    i += delta
    i %= 26
    l = chr(i + ord('a'))
    print("conv to ", l)
    return l

def to_encrypt(text, delta):
    print("Task: ", text, " shifted on ", delta)
    res_str = ""
    for c in text:
        if c != ' ':
            res_str += encr_letter(c, delta)
        else:
            res_str += c
    print ("result str: ", res_str)
    print("")
    return res_str

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
