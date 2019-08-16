"""
    Sort by count O(n +M)
    Первая строка содержит число 1≤n≤104, вторая — n натуральных чисел, не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.
    Sample Input:
    5
    2 3 9 2 9
    Sample Output:
    2 2 3 9 9
    Algo:
    A -- array [0,n) with int from 1 to M, s = 1
    create array B from 0 to M-1 <- [0,..,0]
    for j from 0 to n-1:
        B[A[j]-s] += 1
    for i from 1 to M-1:
        B[i] += B[i-1]
    for j = n-1 to 0:
        A'[B[A[j]-s]] = A[j]
        B[A[j]-s] -= 1
"""

def count_sort(A, m):
    s = 1
    n = len(A)
    b = [0 for i in range(m)]
    res = [0 for i in range(n)]
    for a in A:
        b[a-s] += 1
    for i in range(1, m):
        b[i] += b[i-1]
    for i in range(m):
        b[i] -= 1
    for j in range(n-1, -1, -1):
        res[b[A[j]-s]] = A[j]
        b[A[j]-s] -= 1
    return res
    

if __name__ == "__main__":
    input()
    nums = [int(w) for w in input().split()]
    nums_s = count_sort(nums, 10)
    for n in nums_s:
        print(n, end=" ")
