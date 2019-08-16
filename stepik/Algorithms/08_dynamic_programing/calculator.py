"""
    Simple calculator: x -> 2x, x -> 3x, x -> x+1
    У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x: заменить x на 2x, 3x или x+1. По данному целому числу 1≤n≤105 определите минимальное число операций k, необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.
    Sample Input 1:
    1
    Sample Output 1:
    0
    1 
    Sample Input 2:
    5
    Sample Output 2:
    3
    1 2 4 5 
    Sample Input 3:
    96234
    Sample Output 3:
    14
    1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234 
"""

def calculator(n):
    if n == 1: return [1]
    d = [0 for i in range(n+1)]
    for i in range(2, n+1):
        l2 = 100000
        l3 = 100000
        if i % 2 == 0:
            l2 = d[i//2]
        if i % 3 == 0:
            l3 = d[i//3]
        d[i] = 1 + min(d[i-1], l2, l3)
    # path
    nums = [n]
    i = n
    while i > 1:
        k = i - 1
        dmin = d[k]
        if i % 2 == 0 and dmin > d[i//2]:
            k = i//2
            dmin = d[k]            
        if i % 3 == 0 and dmin > d[i//3]:
            k = i//3
            dmin = d[k]        
        nums.append(k)
        i = k
    return nums

def test():
    #print(calculator(96234))
    assert len(calculator(1))-1 == 0
    assert len(calculator(5))-1 == 3
    assert len(calculator(96234))-1 == 14
    

if __name__ == "__main__":
    test()
    n = int(input())
    nums = calculator(n)
    print(len(nums)-1)
    for n in nums[::-1]:
        print(n, end = ' ')
        
    
