"""
    Editing distance
    Вычислите расстояние редактирования двух данных непустых строк длины не более \( 10^2 \), содержащих строчные буквы латинского алфавита.

    Sample Input 1:
    ab
    ab
    Sample Output 1:
    0
    Sample Input 2:
    short
    ports
    Sample Output 2:
    3
    
    Algo:
    Input data: a[0..n-1], b[0..m-1]
    d[0..n][0..m]
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1)
        d[0][j] = j
    for i in range(n):
        for j in range(m):
            c = a[i] == b[j] ? 0 : 1
            d[i+1][j+1] = min(d[i][j+1]+1, d[i+1][j]+1, d[i][j] + c)
    return d[n][m]
"""

def findEditingDistance(a, b):
    n = len(a)
    m = len(b)
    if n == 0 and m == 0: return 0
    d = []
    for i in range(n+1):
        d.append([0 for j in range(m+1)])
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j
    for i in range(n):
        for j in range(m):
            c = 0 if a[i] == b[j] else 1
            d[i+1][j+1] = min(d[i][j+1]+1, d[i+1][j]+1, d[i][j] + c)
    return d[n][m]

def test():
    assert findEditingDistance("", "") == 0
    assert findEditingDistance("ab", "ab") == 0
    assert findEditingDistance("short", "ports") == 3
    assert findEditingDistance("editing", "distance") == 5

if __name__ == "__main__":
    test()
    a, b = input(), input()
    print(findEditingDistance(a, b))
