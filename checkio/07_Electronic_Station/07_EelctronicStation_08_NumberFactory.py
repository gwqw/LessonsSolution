def add_num_left(a, b):
    a = str(a)
    b = str(b)
    res = a + b
    return int(res)

def checkio(number):
    if number <= 9: return number
    # calc dividers
    dividers = [i for i in range(9,1,-1) if number % i == 0]
    if not dividers:
        return 0
    dividers.sort()

    # find multiplyer for each number
    res_lst = []
    for i in dividers:
        add = checkio(number//i)
        if add == 0: return 0
        res_lst.append(add_num_left(i, add))
    if not res_lst:
        return 0
    res_lst.sort()        
    return res_lst[0]
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
