"""
Input:
n m # n -- number of table, m -- numer of requests
r1 r2 .. rm # sizes of tables
d s # request to table union: d -- number of destination table, s -- number of source table
output:
max_size_j # max_size of table after the j-th request
"""

import sys

class DJSet:
    def __init__(self, max_size):
        self.parent = []
        self.size = []
        self._resize_(max_size+1)
        self.maxim = 0

    def _resize_(self, size):
        if len(self.parent) < size:
            self.parent += [None] * (size - len(self.parent))
            self.size += [None] * (size - len(self.size))

    def make_set(self, i, size):
        self.parent[i] = i
        self.size[i] = size
        if size > self.maxim: self.maxim = size

    def find1(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # i -- dest, j -- source
        i_id, j_id = self.find(i), self.find(j)
        if i_id == j_id: return self.maxim
        self.parent[j_id] = i_id
        self.size[i_id] += self.size[j_id]
        if self.size[i_id] > self.maxim: self.maxim = self.size[i_id]
        return self.maxim
            
    def print(self):
        print(self.parent[1:], self.size[1:])


def simple_test1():
    # example 1
    output = []
    st = DJSet(5)
    st.make_set(1, 1)
    st.make_set(2, 1)
    st.make_set(3, 1)
    st.make_set(4, 1)
    st.make_set(5, 1)
    output.append(st.union(3, 5))#; st.print()
    output.append(st.union(2, 4))#; st.print()
    output.append(st.union(1, 4))#; st.print()
    output.append(st.union(5, 4))#; st.print()
    output.append(st.union(5, 3))#; st.print()
    #print(output)
    assert(output == [2, 2, 3, 5, 5])

    # example 2
    output = []
    st = DJSet(6)
    st.make_set(1, 10)
    st.make_set(2, 0)
    st.make_set(3, 5)
    st.make_set(4, 0)
    st.make_set(5, 3)
    st.make_set(6, 3)
    output.append(st.union(6, 6))
    output.append(st.union(6, 5))
    output.append(st.union(5, 4))
    output.append(st.union(4, 3))
    #print(output)
    assert(output == [10, 10, 10, 11])

if __name__ == "__main__":
    simple_test1()
    n, m = (int(s) for s in input().split())
    # disjoint sets creation
    st = DJSet(n)
    dset = [int(s) for s in input().split()]
    for i,s in enumerate(dset):
        st.make_set(i+1, s)
    # requests
    reader = (line.split() for line in sys.stdin)
    i = 0
    output = []
    for words in reader:
        if len(words) == 2:
            output.append(st.union(int(words[0]), int(words[1])))
        i += 1
        if i == m: break
    # output
    for o in output:
        print(o)
    

    

