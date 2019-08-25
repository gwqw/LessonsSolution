"""
    Express n as consecutive sum from k to m. Simple Example 42 = sum from 42 to 42
    input: n
    output: num of sums
"""

import math

def sum_ft(k, m):
    return m*(m+1)/2 - k*(k-1)/2

def count_consecutive_summers(num):
    res = 1 # k = m = n
    for m in range (num//2+1, int(math.sqrt(num)), -1):
        for k in range(m-1, 0, -1):
            if sum_ft(k, m) == num:
                res += 1
            elif sum_ft(k, m) > num:
                break
    return res


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
