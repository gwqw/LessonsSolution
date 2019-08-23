def time_sec(tme):
    h,m = tme.split(':')
    h = int(h)
    m = int(m)
    return h*60 + m

def max_idx(lst):
    idx = 0
    max_value = 0
    for i,l in enumerate(lst):
        if l > max_value:
            idx = i
            max_value = l
    return idx

def min_idx(lst):
    idx = 0
    min_value = 999
    for i,l in enumerate(lst):
        if l < min_value:
            idx = i
            min_value = l
    return idx

def fastest_horse(horses: list) -> int:
    h_values = [0 for t in horses[0]]
    for t in horses:
        h_values[min_idx([time_sec(i) for i in t])] += 1
    print(h_values)
    return max_idx(h_values)+1

if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    assert fastest_horse([["1:10","1:15","1:20"],["1:05","1:10","1:15"],["2:59","2:59","2:59"]]) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
