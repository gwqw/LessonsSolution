"""
Двоичный поиск
В первой строке даны целое число 1≤n≤105 и массив A[1…n] из n различных натуральных чисел, не превышающих 109, в порядке возрастания, во второй — целое число 1≤k≤105 и k натуральных чисел b1,…,bk, не превышающих 109. Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.
Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11
Sample Output:
3 1 -1 1 -1
"""

def get_pos(numbers, n):
    if len(numbers) == 0: return -1
    l, r = 0, len(numbers)-1
    while l <= r:
        m = l + (r - l) // 2
        if numbers[m] == n:
            return m+1
        elif numbers[m] > n:
            r = m - 1
        else:
            l = m + 1
    return -1

if __name__ == "__main__":
    words = input().split()
    numbers = [int(w) for w in words]
    numbers.pop(0)
    words = input().split()
    test_numbers = [int(w) for w in words]
    test_numbers.pop(0)

    for n in test_numbers:
        print(get_pos(numbers, n), end = " ")
    
