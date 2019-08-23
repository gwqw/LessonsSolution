def find_new_pos(s, p):
    return s.find(p)

def find_new_pos_list(s, plist):
    for i in range(len(s)):
        if s[i] in plist: return i
    return -1

def createRange(pat_list, e):
    b = pat_list[-1]
    for p in range(ord(b)+1, ord(e)):
        pat_list.append(chr(p))

def unix_match(filename: str, pattern: str) -> bool:
    print(filename, " ", pattern)
    i = 0
    is_find = False
    is_bracket = False
    pat_list = []
    is_not = False
    for idx, p in enumerate(pattern):
        if i >= len(filename):
            print("different length")
            return False
        
        #print(p, " ", filename[i])
        if p == '[' and not is_bracket:
            pat_list = []
            is_bracket = True
            is_not = False
            continue
        if p == ']':
            if pat_list or ']' not in pattern[idx+1:]:
                if not is_bracket and p == filename[i]:
                    i += 1
                    continue
                if pat_list == ['!']:
                    if filename[i:i+3] == "[!]":
                        i += 3
                        continue
                    else:
                        print(filename[i:i+3])
                        return False
                if is_find:
                    j = find_new_pos_list(filename[i:], pat_list)
                    if j == -1:
                        print(f"No symbol of {filename[i:]} in {pat_list}")
                        return False
                    i += j + 1
                    is_find = False
                else:
                    if not ((filename[i] in pat_list) ^ is_not):
                        print(f"No symbol {filename[i]} in {pat_list}")
                        return False
                is_bracket = False
                i += 1
                continue

        if p == '*' and not is_bracket:
            is_find = True
            continue
        if p == '?' and not is_bracket:
            if not is_find:
                i += 1
            continue        
        
        if is_bracket:
            if p == '!': is_not = True
            if p == '-' and pat_list:
                createRange(pat_list, pattern[idx+1])
            pat_list.append(p)
        elif is_find:
            j = find_new_pos(filename[i:], p)
            if j == -1:
                print(f"No symbol {filename[i:]} in {p}")
                return False
            i += j + 1
            is_find = False
        else:
            if p != filename[i]:
                print(f"{filename[i]} != {p}")
                return False
            i += 1
    return True


if __name__ == '__main__':
    print("Example:")
    # These "asserts" are used for self-checking and not for an auto-testing
    """
    print("")
    print("Full match ")
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('somefile.txt', 'somefile1.txt') == False
    assert unix_match('somefile1.txt', 'somefile.txt') == False
    print("")
    print("test ?")
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    print("")
    print("test *")
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.txt', '*.txt') == True
    assert unix_match('my.exe', '*.txt') == False
    print("")
    print("test []")
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    print("")
    print("test [!]")
    assert unix_match("1name.txt","[!abc]name.txt") == True
    print("")
    print("Complex tests")
    assert unix_match("txt","????*") == False
    assert unix_match("apache12.log","*[1234567890].*") == True
    
    assert unix_match("[!]check.txt","[!]check.txt") == True
    """
    assert unix_match("[?*]","[[][?][*][]]") == True
    assert unix_match("Feb 2018","[A-Z][a-z][a-zA-Z] [2-3][0-4][1-1][5-9]") == True
    assert unix_match("[check].txt","[][]check[][].txt") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
