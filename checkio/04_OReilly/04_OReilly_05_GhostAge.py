def give_fibonacci():
    res = [1, 1]
    while True:
      res.append(res[-1] + res[-2])
      yield res[-3]

def get_age_opacity(op):
    if op == 10000: return 0
    # create fibonacci list
    fibonacci = []
    generator = give_fibonacci()
    for i in range(1000):
        fibonacci.append(next(generator))

    # find need opacity
    opacity = [10000]
    for year in range(1,5000):
        if year in fibonacci:
            k = -year
        else:
            k = +1
        opacity.append(opacity[-1] + k)
        if opacity[-1] == op:
            return year
    
def checkio(opacity):
    return get_age_opacity(opacity)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
