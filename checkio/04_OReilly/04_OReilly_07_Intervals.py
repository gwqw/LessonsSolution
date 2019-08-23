def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    data = list(data)
    data.sort()
    res = []
    for d in data:
        for l,h in res:
            if d >= l and d <= h:
                break
            if l-d == 1:
                res.remove((l, h))
                res.append((l-1,h))
                break
            if d-h == 1:
                res.remove((l, h))
                res.append((l, h+1))
                break
        else:
            res.append((d, d))
    res.sort()
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals([8,9,6,7]) == [(6,9)], "Third"
    print('Almost done! The only thing left to do is to Check it!')
