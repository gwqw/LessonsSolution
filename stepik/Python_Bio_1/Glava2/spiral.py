"""
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

Algo:
1) fill top row
2) fill right column
3) fill down backward
4) fill left column to up
mtx = []

"""

if __name__ == "__main__":
     l = [0 for x in range(10)]
     print(l)
     
