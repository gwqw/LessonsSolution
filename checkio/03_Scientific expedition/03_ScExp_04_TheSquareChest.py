def check_one_square(l, i):
    # top
    res = [i, i+1] in l
    # left
    res = res and [i, i+4] in l
    # right
    res = res and [i+1, i+5] in l
    # down
    res = res and [i+4, i+5] in l
    return res

def check_two_square(l, i):
    # top
    res = [i, i+1] in l and [i+1, i+2] in l
    # left
    res = res and [i, i+4] in l and [i+4, i+8] in l
    # right
    res = res and [i+2, i+2+4] in l and [i+2+4, i+2+8] in l
    # down
    res = res and [i+8, i+9] in l and [i+9, i+10] in l
    return res

def check_three_square(l, i):
    # top
    res = [i, i+1] in l and [i+1, i+2] in l and [i+2, i+3] in l
    # left
    res = res and [i, i+4] in l and [i+4, i+8] in l and [i+8, i+12] in l
    # right
    res = res and [i+3, i+3+4] in l and [i+3+4, i+3+8] in l and [i+3+8, i+3+12] in l
    # down
    res = res and [i+12, i+13] in l and [i+13, i+14] in l and [i+14, i+15] in l
    return res

def checkio(lines_list):
    """Return the quantity of squares"""
    # bruteforce
    lines_list.sort()
    for i in lines_list:
        i.sort()
    # 1x1 square
    square_count = 0
    for i in range(1,4):
        for j in range(0,3):
            if check_one_square(lines_list, i+j*4):
                #print("1x1: " + str(i+j*4))
                square_count += 1
    # 2x2 square
    for i in range(1,3):
        for j in range(0,2):
            if check_two_square(lines_list, i+j*4):
                square_count += 1
                #print("2x2: " + str(i+j*4))
    # 3x3 square
    if check_three_square(lines_list, 1):
        square_count += 1
        #print("3x3")
    #print(square_count)
    return square_count

if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    assert (checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],
                     [14,13],[13,9],[15,14]]) == 3), "3 square low"
