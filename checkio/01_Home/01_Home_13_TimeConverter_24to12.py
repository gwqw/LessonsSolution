"""
    Time Converter (24h to 12h)
    Convert 24-h format to 12-h format
    Input: hh:mm # 24-hour string 
    output: hh:mm a.m. or p.m. # 12-h format
    if hours < 10: output wo first 0    
"""

def time_converter(time):
    h, m = (int(s) for s in time.split(':'))
    if h >= 12:
        st = "p.m."
    else:
        st = "a.m."
    if h > 12:
        h -= 12
    elif h == 0:
        h = 12
    return "%d:%02d %s" % (h, m, st)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
    print(time_converter('09:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
