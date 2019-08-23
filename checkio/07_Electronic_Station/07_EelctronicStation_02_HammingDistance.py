def add_zeros(n, m):
    if len(n) > len(m):
        m = (len(n) - len(m))*'0' + m
    return m

def checkio(n, m):
    if n == m: return 0
    if n < m: n,m = m,n

    # form binary strings
    n = bin(n)[2:]
    m = bin(m)[2:]
    m = add_zeros(n, m)

    # count difference
    diff = 0
    for c1,c2 in zip(n, m):
        if c1 != c2: diff += 1

    return diff

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    print("Gut!")
