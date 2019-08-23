def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) > 1:
        l = args
    else:
        l = list(args[0])
    min_res = l[0]
    for i in l:
        if key:
            if key(i) < key(min_res):
                min_res = i
        else:
            if i < min_res:
                min_res = i
    print(min_res)
    return min_res


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) > 1:
        l = args
    else:
        l = list(args[0])
    max_res = l[0]
    for i in l:
        if key:
            if key(i) > key(max_res):
                max_res = i
        else:
            if i > max_res:
                max_res = i
    print(max_res)
    return max_res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
