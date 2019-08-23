def checkio(str_number, radix):
    power = 0
    res = 0
    for i in range(len(str_number)-1, -1, -1):
        d = str_number[i]
        if d.isdigit():
            d = int(d)
        else:
            d = ord(d) - ord('A') + 10
        if d >= radix: return -1
        res += d * radix**power
        power += 1
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
