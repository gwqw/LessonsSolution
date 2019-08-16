"""
Find all positions of Pattern in Text (algorithm Rabin-Karp)
Input:
Pattern
Text
Out: pos1 pos2 ...

"""

import random

P = 1000000007

def get_xm1(x, m, p):
    if m == 1: return 1
    r = x
    for i in range(m-2):
        r *= x
        r %= p
    return r

def hashf(s, x, p):
    if not s: return 0
    r = ord(s[-1])
    for i in range(len(s)-2,-1,-1):
        r = r * x + ord(s[i])
        r %= p
    return r

def find_text(pattern, text):
    m, n = len(pattern), len(text)
    x = random.randint(1, P)    
    xm1 = get_xm1(x, m, P)
    hp = hashf(pattern, x, P)
    hw = hashf(text[-m : n], x, P)
    #print("hash_pattern=", hp)
    #print("hash_w_last=", hw)
    output = []
    if hp == hw and pattern == text[n-m : n]:
        output.append(n-m)
    for i in range(n-m-1, -1, -1):
        hw = (hw - ord(text[i+m]) * xm1) * x + ord(text[i])
        hw %= P
        #print("hash_w for", i, "=", hw, "window=", text[i : i+m])
        if hp == hw and pattern == text[i : i+m]:
            output.append(i)
    return list(reversed(output))
        
    

def test_example():
    #print(find_text("aba", "abacaba"))
    assert(find_text("aba", "abacaba") == [0, 4])
    assert(find_text("Test", "testTesttesT") == [4])
    assert(find_text("aaaaa", "baaaaaaa") == [1, 2, 3])
    #print(find_text("algorithm", "In computer science, the Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching algorithm created by Richard M. Karp and Michael O. Rabin (1987) that uses hashing to find any one of a set of pattern strings in a text. For text of length n and p patterns of combined length m, its average and best case running time is O(n+m) in space O(p), but its worst-case time is O(nm). In contrast, the Aho–Corasick string-matching algorithm has asymptotic worst-time complexity O(n+m) in space O(m)."))
    assert(find_text("algorithm", "In computer science, the Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching algorithm created by Richard M. Karp and Michael O. Rabin (1987) that uses hashing to find any one of a set of pattern strings in a text. For text of length n and p patterns of combined length m, its average and best case running time is O(n+m) in space O(p), but its worst-case time is O(nm). In contrast, the Aho–Corasick string-matching algorithm has asymptotic worst-time complexity O(n+m) in space O(m).") == [36, 60, 92, 432])
    #print(find_text("a", "abacaba"))
    assert(find_text("a", "abacaba") == [0, 2, 4, 6])
    assert(find_text("ab", "abacaba") == [0, 4])

if __name__ == "__main__":
    test_example()
    
    pattern = input()
    text = input()
    output = find_text(pattern, text)
    print(' '.join(str(i) for i in output))
