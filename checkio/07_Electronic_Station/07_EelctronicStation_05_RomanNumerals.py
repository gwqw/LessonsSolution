def conv_rom(d, one, five, ten):
    if d <= 3: return d*one
    if d == 4: return one+five
    if d <= 8: return five+one*(d-5)
    return one+ten

def checkio(data):
    # thousands
    th = data // 1000
    res = th * 'M'
    # hundreds
    hun = (data - th * 1000) // 100
    res += conv_rom(hun, 'C', 'D', 'M')
    # tens
    tens = (data - th*1000 - hun*100) // 10
    res += conv_rom(tens, 'X', 'L', 'C')
    # ones
    ones = (data - th*1000 - hun*100 - tens*10) // 1
    res += conv_rom(ones, 'I', 'V', 'X')
    
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
