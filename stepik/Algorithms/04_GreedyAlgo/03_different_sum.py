"""
По данному числу 1≤n≤10^9 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:
4
Sample Output 1:
2
1 3 
Sample Input 2:
6
Sample Output 2:
3
1 2 3 

"""

def diff_sum(n):
    # for i in n:
    #   if n-i > i
    #       insert i
    #       n -= i
    #   else:
    #       insert n
    # return v
    v = []
    i = 1
    while True:
        if n-i > i:
            v.append(i)
            n -= i
            i += 1
        else:
            v.append(n)
            return v    

def main():
    n = int(input())
    v = diff_sum(n)
    print(len(v))
    for i in v:
        print(i, end=" ")
    

if __name__ == "__main__":
    main()
