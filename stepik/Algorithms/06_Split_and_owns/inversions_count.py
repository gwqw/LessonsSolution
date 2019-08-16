"""
Подсчитать число инверсий
Первая строка содержит число 1≤n≤105, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 109. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j]. (Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
Sample Input:
5
2 3 9 2 9
Sample Output:
2
"""

def count_inversions_simple(a):
    # simple
    inv_cnt = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                inv_cnt += 1
    return inv_cnt

def merge(a1, a2):
    arr = []
    inv = 0
    j, k = 0, 0
    for i in range(0, len(a1) + len(a2)):
        if j == len(a1):
            arr.extend(a2[k:])
            break
        if k == len(a2):
            arr.extend(a1[j:])
            #inv += (len(a1) - j) * len(a2)
            break
        if a1[j] > a2[k]:
            arr.append(a2[k])
            k += 1
            inv += len(a1) - j
        else:
            arr.append(a1[j])
            j += 1
    return arr, inv

def count_inversions(a):
    if len(a) <= 1:
        return a, 0

    m = len(a) // 2
    a1, i1 = count_inversions(a[:m])
    a2, i2 = count_inversions(a[m:])
    a, i = merge(a1, a2)
    return a, i + i1 + i2


if __name__ == "__main__":
    n = int(input())
    words = input().split()
    arr = [int(w) for w in words]
    print(count_inversions(arr)[1])
