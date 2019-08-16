"""
Поиск скольким отрезкам принадлежит точка
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно. Следующие n строк содержат по два целых числа ai и bi (ai≤bi) — координаты концов отрезков. Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 108 по модулю. Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
Sample Input:
2 3
0 5
7 10
1 6 11
Sample Output:
1 0 0

Algo:
- find all segments with lp lesser than p (l). l == all left segments + cross
- find all segments with rp higher than p (r). r == all right segments + cross
- l + r = n + cross
- cross = l + r - n
"""

import bisect

def count_segments(segments_left, segments_right, p):
    n = len(segments_right)
    l = bisect.bisect(segments_left, p) 
    r = n - bisect.bisect_left(segments_right, p)
    return r + l - n


if __name__ == "__main__":
    words = input().split()
    n,m = int(words[0]), int(words[1])
    # segments reading
    segments_left = []
    segments_right = []
    for i in range(n):
        words = input().split()
        x,y = int(words[0]), int(words[1])
        segments_left.append(x)
        segments_right.append(y)

    #sort
    segments_left.sort()
    segments_right.sort()
    # points reading
    words = input().split()
    points = [int(w) for w in words]

    # find segments num
    for p in points:
        print(count_segments(segments_left, segments_right, p), end = " ")
    
