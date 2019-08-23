import operator

def decToBin(num):
    resBin = []
    while num:
        resBin.append(num % 2)
        num //= 2
    resBin.reverse()
    return resBin

def binToDec(num):
    num.reverse()
    res = 0
    for i,n in enumerate(num):
        res += n << i
    return res

def andNums(first, second, op):
    res = []
    for f in first:
        t = []
        for s in second:
            t.append(op(f, s))
        print(t)
        res.append(binToDec(t))
    print(res)
    res = sum(res)
    print(res)
    return res

def checkio(first, second):
    f = decToBin(first)
    s = decToBin(second)
    andNum = andNums(f, s, operator.and_)
    orNum = andNums(f, s, operator.or_)
    xorNum = andNums(f, s, operator.xor)
    res = andNum + orNum + xorNum
    print("res= ", res)
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
