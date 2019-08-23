import math

def sph_oblate_area(c, a):
    e = math.sqrt(1 - (c/a)**2)
    return 2*math.pi * a**2 * (1 + (1 - e**2)/e * math.atanh(e))

def sph_prolate_area(c, a):
    e = math.sqrt(1 - (a/c)**2)
    return 2*math.pi * a**2 * (1 + c/(a * e) * math.asin(e))

def sph_area(r):
    return 4*math.pi * r**2

def spheroid_area(c, a):
    if c < a:
        return sph_oblate_area(c, a)
    elif c > a:
        return sph_prolate_area(c, a)
    else:
        return sph_area(c)

def spheroid_volume(height, width):
    return 4*math.pi/3 * width**2 * height

def checkio(height, width):
    r = lambda a: round(a * 100)/100
    volume = r(spheroid_volume(height/2, width/2))
    area = r(spheroid_area(height/2, width/2))
    return [volume, area]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
