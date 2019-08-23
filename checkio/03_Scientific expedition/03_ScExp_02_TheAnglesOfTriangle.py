import math

def calc_alpha(a, b, c):
    alpha = ((b**2 + c**2) - a**2) / (2*b*c)
    if abs(alpha) < 1:
        alpha = math.acos(alpha) * 180 / 3.14159
    else:
        alpha = 0
    return round(alpha)

def checkio(a, b, c):
    # cos theorem: a**2 = b**2 + c**2 - 2*b*c*cos(alpha)
    # cos(alpha) = (a**2 - (b**2 + c**2) / (2*b*c))
    alpha = calc_alpha(a, b, c)
    beta = calc_alpha(b, a, c)
    gamma = calc_alpha(c, a, b)
    res = [alpha, beta, gamma]
    res.sort()
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(10,20,30) == [0, 0, 0], "It's can not be a triangle"
