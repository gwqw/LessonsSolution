"""
Parallel treatment of tasks
Input:
m n # n -- number of processs, m -- number of tasks
t0,..,tm-1 # array of times needed for treatment of i-th task
Output:
p0 st0 # 
..
stm-1 stm-1 # start time for task treatment

Ex.1:
2 5
1 2 3 4 5
out:
0 0
1 0
0 1
1 2
0 4

Ex.2: (look at the task)

algo:
heap: time -- priority, process number is secod priority
"""

import heapq

def get_numbers(a, m):
    lst = [(0, i) for i in range(m)]
    output = []
    heapq.heapify(lst)
    for t in a:
        p = heapq.heappop(lst)
        output.append((p[1], p[0]))
        p = (p[0] + t, p[1])
        heapq.heappush(lst, p)
    return output

def test_example():
    output = get_numbers([1, 2, 3, 4, 5], 2)
    #print(output)
    assert(output == [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)])
    output = get_numbers([1]*20, 4)
    #print(output)
    assert(output == [(0, 0), (1, 0), (2, 0), (3, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4),
                    ])
    
if __name__ == "__main__":
    test_example()
    m, n = (int(s) for s in input().split())
    a = [int(s) for s in input().split()]
    output = get_numbers(a, m)
    for o in output:
        print(o[0], o[1])


    
