def conv_to_morse(b):
    if b: return '-'
    else: return '.'

def digit_to_code(n, p):
    res = ""
    for i in range(p-1,-1,-1):
        r = n // 2**i
        #print(i, n, r)
        res += conv_to_morse(r)
        n -= r * 2**i
    #print(res)
    return res

def num_to_code(n):
    f = n // 10
    s = n - f*10
    return digit_to_code(f, 3) + ' ' + digit_to_code(s, 4)

def checkio(time_string):
    l = time_string.split(':')
    h = int(l[0])
    m = int(l[1])
    s = int(l[2])
    # hours
    print(h, m, s, sep=':')
    res = num_to_code(h)
    res = res[1:]
    # minutes
    res += " : " + num_to_code(m)
    # secundes
    res += " : " + num_to_code(s)
    print(res)    
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
