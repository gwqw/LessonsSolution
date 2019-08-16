"""
Первая строка содержит количество предметов 1≤n≤10^3
и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6
и объём 0<wi≤2⋅10^6 предмета (n, W, ci, wi — целые числа).
Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть, стоимость и объём
при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000
"""

class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w

def get_max_knapsack_value(capacity, items):
    # sort by c/w
    # while sum_weigth < W:
    #   sum_weight += wi max to W
    #   value += part (c)
    # return value
    items.sort(key =
        lambda item: float(item.value) / item.weight,
        reverse = True
    )
    #print(items)
    value = 0.0
    for item in items:
        if capacity > item.weight:
            capacity -= item.weight
            value += item.value
        else:
            value += item.value * float(capacity) / item.weight
            break
    return value
    

def main():
    words = input().split()
    n, capacity = int(words[0]), int(words[1])
    items = []
    for i in range(n):
        words = input().split()
        a,b = int(words[0]), int(words[1])
        items.append(Item(a, b))
    max_value = get_max_knapsack_value(capacity, items)
    print(max_value)
    


if __name__ == "__main__":
    main()
