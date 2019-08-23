def checkio(first, second):
    s1 = set(first.split(','))
    s2 = set(second.split(','))
    common = list(s1 & s2)
    if common:
        common.sort()
        res = ''
        for i in common:
            res += i
            if i != common[-1]:
                res += ','
        return res
    else:
        return ""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
