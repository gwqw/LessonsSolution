"""
    LIS -- наибольшая возрастающая последовательность
    Algo:
    Input: a -- array of number length n
    d[0..n-1], prev[0..n-1]
    for i in range(n):
        d[i] = 1
        prev[i] = -1
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    ans = 0
    for i in range(n):
        ans = max(ans, d[i])
    return ans
"""

import operator

def lis(a, op):
    n = len(a)
    d = [0 for i in range(n)]
    prev = [0 for i in range(n)]
    for i in range(n):
        d[i], prev[i] = 1, -1
        for j in range(i):
            if op(a[j], a[i]) and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    ans = 0
    ans = max(d)
    return ans

def test():
    assert lis([7, 2, 1, 3 ,8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1], operator.lt) == 5

def div_func(a, b):
    return b % a == 0


if __name__ == "__main__":
    test()
    input()
    numbers = [int(w) for w in input().split()]
    print(lis(numbers, div_func))
        
        
