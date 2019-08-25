"""
    Convert time from 12h format to 24h
    h:mm a.m. or p.m. -> hh:mm
"""

def time_converter(time):
    w, state = time.split()
    h, m = w.split(':')
    h = int(h)
    if state == "p.m." and h != 12:
        h += 12
    elif state == "a.m." and h == 12:
        h = 0
    return "%02d:%s" % (h, m)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
