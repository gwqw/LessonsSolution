"""
    Group Equal consecutive
    group each element in list and add all lists to one list and return
    Input: List of str and int
    Output: List of lists of str and int 
"""

def group_equal(els):
    res = []
    for e in els:
        if not res or e not in res[-1]:
            res.append([])
        res[-1].append(e)
    return res


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
