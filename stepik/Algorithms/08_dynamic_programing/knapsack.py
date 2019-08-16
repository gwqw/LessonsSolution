"""
    KnapSack
    Первая строка входа содержит целые числа 1≤W≤104 и 1≤n≤300 — вместимость рюкзака и число золотых слитков. Следующая строка содержит n целых чисел 0≤w1,…,wn≤105, задающих веса слитков. Найдите максимальный вес золота, который можно унести в рюкзаке.
    Sample Input:
    10 3
    1 4 8
    Sample Output:
    9

    Algo:
    Input: W, wi[1..n], ci[1..n]
    d[0..W][0..n]
    for w in range(W+1):
        d[w][0] = 0
    for i in range(n+1):
        d[0][i] = 0
    for i in range(1, n+1):
        for w in range(1, W+1):
            d[w][i] = d[w][i-1]
            if wi[i] <= w:
                d[w][i] = max(d[w][i], d[w-wi[i]][i-1] + ci[i])
    return d[W,n]
    sashik, dimik
"""

def knapsack_wo_repeat(W, wi, ci):
    n = len(wi)
    wi = [0] + wi
    ci = [0] + ci
    d = []
    for i in range(W+1):
        d.append([0 for j in range(n+1)])
    for w in range(W+1):
        d[w][0] = 0
    for i in range(n+1):
        d[0][i] = 0
    for i in range(1, n+1):
        for w in range(1, W+1):
            d[w][i] = d[w][i-1]
            if wi[i] <= w:
                d[w][i] = max(d[w][i], d[w - wi[i]][i-1] + ci[i])
    return d[W][n]
    

def test():
    assert knapsack_wo_repeat(10, [1, 4, 8], [1, 4, 8]) == 9

if __name__ == "__main__":
    test()    
    W, n = (int(w) for w in input().split())
    wi = [int(w) for w in input().split()]
    print(knapsack_wo_repeat(W, wi, wi))
