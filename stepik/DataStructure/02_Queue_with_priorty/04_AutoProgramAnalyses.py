"""
xi == xj and xp != xq
Input:
n, e, d # n -- variables number, e -- strings number: xi == xj, d -- strings numer: xi != xj
i j
Output:
1 or 0 # 1 -- possible, 0 -- impossible

Ex.1
4 6 0
1 2
1 3
1 4
2 3
2 4
3 4
out: 1 # all variables are equal

Ex.2
6 5 3
2 3
1 5
2 5
3 4
4 2
6 1
4 6
4 5
out: 0 # x1 == x2 == x3 == x4 == x5, but x4 != x5
"""

import sys

class DJSet:
    def __init__(self, max_size):
        self.parent = []
        self.rank = []
        self._resize_(max_size+1)
        for i in range(1, max_size+1):
            self.make_set(i)

    def _resize_(self, size):
        if len(self.parent) < size:
            self.parent += [None] * (size - len(self.parent))
            self.rank += [None] * (size - len(self.rank))

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find1(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        if i_id == j_id: return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        elif self.rank[i_id] < self.rank[j_id]:
            self.parent[i_id] = j_id
        else:
            self.parent[j_id] = i_id
            self.rank[i_id] += 1
            #self.parent[i_id] = j_id
            #self.rank[j_id] += 1

    def union1(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        if i_id == j_id: return
        self.parent[j_id] = i_id
        self.rank[i_id] = max(self.rank[i_id], 1 + self.rank[j_id])
            
    def print(self):
        print(self.parent[1:], self.rank[1:])

    def check(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        return i_id != j_id

def check(n, equals, dis_equals):
    st = DJSet(n)
    for i,j in equals:
        st.union(i, j)
    for i,j in dis_equals:
        if st.check(i, j) == 0:
            return 0
    return 1

def test_example():
    # example 1
    st = DJSet(6)
    st.union(1, 2)
    st.union(1, 3)
    st.union(1, 4)
    st.union(2, 3)
    st.union(2, 4)
    st.union(3, 4)
    assert(st.check(1, 2) == 0)
    assert(st.check(1, 3) == 0)
    assert(st.check(1, 4) == 0)
    assert(st.check(2, 3) == 0)
    assert(st.check(2, 4) == 0)
    assert(st.check(3, 4) == 0)

    # example 2
    st = DJSet(6)
    st.union(2, 3)
    st.union(1, 5)
    st.union(2, 5)
    st.union(3, 4)
    st.union(4, 2)
    assert(st.check(6, 1) == 1)
    assert(st.check(4, 6) == 1)
    assert(st.check(4, 5) == 0)

def test_example2():
    assert(check(6, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], []) == 1)
    assert(check(6, [(2, 3), (1, 5), (2, 5), (3, 4), (4, 2)], [(6, 1), (4, 6), (4, 5)]) == 0)
    assert(check(6, [], []) == 1)
    

if __name__ == "__main__":
    test_example()
    test_example2()
    n, e, d = (int(s) for s in input().split())
    # request
    reader = (line.split() for line in sys.stdin)
    # equals requests
    k = 0
    equals = []
    if e:
        for i, j in reader:
            equals.append((int(i), int(j)))        
            k += 1
            if k == e: break
        
    # dis_equals requests
    k = 0
    dis_equals = []
    if d:
        for i, j in reader:
            dis_equals.append((int(i), int(j)))        
            k += 1
            if k == d: break
        
        
    # check
    print(check(n, equals, dis_equals))
    


