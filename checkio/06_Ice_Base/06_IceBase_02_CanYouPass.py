def findPath(matrix, first, WAS):
    r, c = first
    val = matrix[r][c]
    res_lst = []
    if r >= 1:
        if val == matrix[r-1][c] and (r-1, c,) not in WAS:
            res_lst.append((r-1,c,))
    if r < len(matrix)-1:
        if val == matrix[r+1][c] and (r+1, c,) not in WAS:
            res_lst.append((r+1,c,))
    if c >= 1:
        if val == matrix[r][c-1] and (r, c-1,) not in WAS:
            res_lst.append((r,c-1,))
    if c < len(matrix[0])-1:
        if val == matrix[r][c+1] and (r, c+1,) not in WAS:
            res_lst.append((r,c+1,))
    WAS.append(first)
    return res_lst

def is_end(matrix, point, second):
    return point == second

def go_through(matrix, first, second, WAS):
    routes = findPath(matrix, first, WAS)
    res = False
    for p in routes:
        if p == second:
            return True
        res = res or go_through(matrix, p, second, WAS)
    return res

def can_pass(matrix, first, second):
    WAS = []
    return go_through(matrix, first, second, WAS)

if __name__ == '__main__':
    print("first")
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    print("second")
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'Second example'
    print("third")
    assert can_pass(((0,0),(0,0)), (0,0), (1,1)) == True, 'Third example'
    
