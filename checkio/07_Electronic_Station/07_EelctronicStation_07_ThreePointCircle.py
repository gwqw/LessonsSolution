import math

def roundTo(v, n):
    mult_pow = 10 ** n
    return round(v / mult_pow) * mult_pow

def coord_parser(data):
    # remove '(' and ')'
    while '(' in data:
        data = data.replace('(', '')
    while ')' in data:
        data = data.replace(')', '')

    # split coordinates
    l = data.split(',')
    return list(map(float, l))
    

def checkio(data):
    coords = coord_parser(data)

    # find coeffs for equations
    a1 = 2*(coords[2] - coords[0])
    b1 = 2*(coords[3] - coords[1])
    a2 = 2*(coords[4] - coords[0])
    b2 = 2*(coords[5] - coords[1])
    c1 = coords[2]**2 - coords[0]**2 + coords[3]**2 - coords[1]**2
    c2 = coords[4]**2 - coords[0]**2 + coords[5]**2 - coords[1]**2

    # find solution
    x0 = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
    if b1 != 0:
        y0 = (c1 - a1*x0) / b1
    elif b2 != 0:
        y0 = (c2 - a2*x0) / b2
    else:
        y0 = 0
    r = (x0 - coords[0])**2 + (y0 - coords[1])**2
    r = math.sqrt(r)
    x0 = roundTo(x0, -2)
    y0 = roundTo(y0, -2)
    r = roundTo(r, -2)
    res = "(x-%g)^2+(y-%g)^2=%g^2" % (x0, y0, r)
    #print(res)
    
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
