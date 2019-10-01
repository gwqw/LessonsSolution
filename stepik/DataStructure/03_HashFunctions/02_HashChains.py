"""
    HashTable with chins. Table with m elements
    h(S) = (Sum from i=0 to S-1 (S[i]*x^i mod p)) mod m
    S[i] -- ASCII code of i-th symbol of string S
    p = 1 000 000 007
    x = 263
    Commands:
        add string # if string exists do not add
        del string # if string exists do not do anything
        find string # yes or no
        check i # output list in i-th cell with space as a separator        
"""

import sys

P = 1000000007

def hashf(s, m, p):
    if not s: return 0
    x = 263
    r = ord(s[-1])
    for i in range(len(s)-2,-1,-1):
        r = r * x + ord(s[i])
        r %= p
    r %= m
    return r

class HashTable:
    def __init__(self, m):
        self.data = [None] * m
        self.m = m

    def add(self, s):
        h = hashf(s, self.m, P)
        l = self.data[h]
        if not l: # empty list
            self.data[h] = [s]
        elif s not in l: # nonempty list and s isn't there
            l.insert(0, s)

    def delete(self, s):
        h = hashf(s, self.m, P)
        l = self.data[h]
        if l and s in l:
            l.remove(s)

    def find(self, s):
        h = hashf(s, self.m, P)
        l = self.data[h]
        return l and s in l

    def check(self, i):
        return self.data[i]

    @staticmethod
    def format_check_res(lst):
        if not lst: return ''
        return ' '.join(lst)

    @staticmethod
    def format_find_res(fr):
        if fr:
            return "yes"
        else:
            return "no"


def test_example():
    h = HashTable(5)
    h.add("world")
    h.add("HellO")
    assert(h.check(4) == ["HellO", "world"])
    assert(not h.find("World"))
    assert(h.find("world"))
    h.delete("world")
    assert(not h.find("world"))
    assert(h.check(4) == ["HellO"])
    h.delete("HellO")
    h.add("luck")
    h.add("GooD")
    assert(h.check(2) == ["GooD", "luck"])
    
    

if __name__ == "__main__":
    test_example()
    m, n = int(input()), int(input())
    reader = (line.split() for line in sys.stdin)
    i = 0
    h = HashTable(m)
    output = []
    if n:
        for words in reader:
            if words[0] == "add":
                h.add(words[1])
            elif words[0] == "del":
                h.delete(words[1])
            elif words[0] == "find":
                output.append(
                    HashTable.format_find_res(h.find(words[1]))
                )
            elif words[0] == "check":
                output.append(
                    HashTable.format_check_res(h.check(int(words[1])))
                )
            i += 1
            if i == n: break
    for o in output:
        print(o)

    
