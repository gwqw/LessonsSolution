"""
Build heap.
Input:
n -- array size
a[0..n-1]
Output:
m -- number of exchanges (0 <= m <= 4n)
i j # exchange elements to make heap (i != j)

Ex.1:
5
5 4 3 2 1
out:
3
1 4
0 1
1 3

Ex.2:
5
1 2 3 4 5
out:
0
"""

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

class MinHeap:
    def __init__(self, a):
        self.data = a
        self.output = []
        self.build_heap()        

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.output.append((i, j))

    def sift_up(self, i):
        pi = i
        while i > 0 and self.data[parent(i)] > self.data[i]:
            pi = parent(i)
            self.swap(pi, i)
            i = pi

    def sift_down(self, i):
        while left(i) < len(self.data):
            min_idx = i
            l = left(i)
            if self.data[l] < self.data[min_idx]:
                min_idx = l
            r = right(i)
            if r < len(self.data) and self.data[r] < self.data[min_idx]:
                min_idx = r
            if i == min_idx: break
            self.swap(i, min_idx)
            i = min_idx

    def build_heap(self):
        n = len(self.data)
        for i in range(n//2-1, -1, -1):
            self.sift_down(i)
    

def build_heap(a):
    heap = MinHeap(a)
    output = heap.output
    return output

def test_example():
    output = build_heap([5, 4, 3, 2, 1])
    #print(output)
    assert(output == [(1, 4), (0, 1), (1, 3)])
    output = build_heap([1, 2, 3, 4, 5])
    #print(output)
    assert(output == [])

if __name__ == "__main__":
    test_example()
    n = int(input())
    a = [int(s) for s in input().split()]
    output = build_heap(a)
    print(len(output))
    for o in output:
        print(o[0], o[1])
    
