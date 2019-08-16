"""
    Даны число 1≤n≤102 ступенек лестницы и целые числа −104≤a1,…,an≤104, которыми помечены ступеньки. Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки), каждый раз поднимаясь на одну или две ступеньки.
    Sample Input 1:
    2
    1 2
    Sample Output 1:
    3
    Sample Input 2:
    2
    2 -1
    Sample Output 2:
    1
    Sample Input 3:
    3
    -1 2 1
    Sample Output 3:
    3
"""

def stairs_recursion(a):
    n = len(a)
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    l1 = stairs(a[:-1])    
    l2 = stairs(a[:-2])
    return a[-1] + max(l1, l2)

def stairs_with_array(a):
    n = len(a)
    if n == 0: return 0
    if n == 1: return a[0]
    d = [0 for i in range(n+1)]
    d[1] = a[0]
    for i in range(2, n+1):
        d[i] = a[i-1] + max(d[i-1], d[i-2])
    return d[-1]

def stairs(a):
    n = len(a)
    if n == 0: return 0
    if n == 1: return a[0]
    prev, cur = 0, a[0]
    for i in range(2, n+1):
        temp = a[i-1] + max(cur, prev)
        prev, cur = cur, temp
    return cur
    

def test():
    assert stairs([1, 2]) == 3
    assert stairs([2, -1]) == 1
    assert stairs([-1, 2, 1]) == 3
    assert stairs([2, -1, -1]) == 1
    assert stairs([-1, -1, -1]) == -2
    assert stairs([0, 0, 0, 4, 6, -5]) == 5
    assert stairs([-64, -16, -13, -9, -48]) == -73
    assert stairs([3, 4, 10, 10, 0, -6, -10, 0]) == 21
    

if __name__ == "__main__":
    #test()
    input()
    nums = [int(w) for w in input().split()]
    print(stairs(nums))
