"""
    You get a plan for a house with '#' and '0' symbols.
    Find area of sqare, wich is rounded the house
    2x2 <= multiline string <= 10x10
    input: multiline-string
    output: area
"""

def house(plan):
    lines = plan.split()
    left = up = 11
    right = down = 0
    for i, line in enumerate(lines):
        l, r = line.find('#'), line.rfind('#')
        if l < left and l > -1: left = l
        if r > right: right = r
        if l > -1 and i < up:
            up = i
        if l > -1 and i > down:
            down = i
    if right >= left and up <= down:
        return (right - left + 1) * (down - up + 1)
    else:
        return 0

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
