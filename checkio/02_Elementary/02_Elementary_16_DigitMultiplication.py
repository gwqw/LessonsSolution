def checkio(number):
    prod = 1
    snum = str(number)
    for ch in snum:
        d = int(ch)
        if d: prod *= d
    return prod

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
