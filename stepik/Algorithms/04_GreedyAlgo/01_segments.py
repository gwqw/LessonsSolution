"""
По данным n

отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100
отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤109,
задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6 
"""

def find_points(segments):
    # sort all segments by right point
    # for every segment:
    #   if left > last_rigth:
    #     add point
    #     last_rigth = right
    #   else:
    #     go further
    segments.sort(key = lambda s: s[1])
    last_right = -1
    res = []
    for l,r in segments:
        if l > last_right:
            res.append(r)
            last_right = r
    return res

def print_points(points):
    print(len(points))
    for p in points:
        print(p, end=" ")

def main():
    n = int(input())
    segments = []
    for i in range(n):
        words = input().split()
        a,b = int(words[0]), int(words[1])
        segments.append([a,b])
    #print(segments)
    points = find_points(segments)
    print_points(points)
    


if __name__ == "__main__":
    main()
