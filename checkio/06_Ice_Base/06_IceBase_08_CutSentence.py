def cut_sentence(line, length):
    print("line: ", line, ", length: ", length)
    line = line.strip()    
    if len(line) <= length:
        print(line)
        return line
    #length -= 1
    cw = ""
    res_line = ""
    for i,c in enumerate(line):
        # add word
        if c == ' ' and i <= length:
            res_line += cw + ' '
            cw = ''
        # out of range
        elif i == length+1:
            res_line = res_line.rstrip()
            if len(res_line) < len(line):
                res_line += "..."
            print(res_line)
            return res_line
        else:
            cw += c
                
    print(res_line)
    return res_line

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    assert cut_sentence("Hi my name is Alex",10) == "Hi my name...", "Fifth"
    print('Done! Do you like it? Go Check it!')
