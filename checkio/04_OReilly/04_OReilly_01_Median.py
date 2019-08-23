def checkio(data):
    data.sort()
    res = 0
    if len(data) % 2 == 0:
        i = len(data) // 2
        res = (data[i-1] + data[i])/2
    else:
        i = (len(data)+1) // 2 -1
        res = data[i]
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
