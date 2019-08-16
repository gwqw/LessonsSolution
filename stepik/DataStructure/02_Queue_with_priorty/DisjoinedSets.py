"""
Input:
n m # n -- number of table, m -- numer of requests
r1 r2 .. rm # sizes of tables
d s # request to table union: d -- number of destination table, s -- number of source table
output:
max_size_j # max_size of table after the j-th request
"""

class DJSet:
    def __init__(self):
        self.parent = []
        self.rank = []

    def _resize_(self, size):
        if len(self.parent) < size:
            self.parent += [None] * (size - len(self.parent))
            self.rank += [None] * (size - len(self.rank))

    def make_set(self, i):
        self._resize_(i+1)
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def find2(self, i):
        if i != self.parent[i]:
            self.parent[i] = find2(self.parent[i])
        return i

    def union_(self, i, j):
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

    def union(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        if i_id == j_id: return
        self.parent[j_id] = i_id
        self.rank[i_id] = max(self.rank[i_id], 1 + self.rank[j_id])
            
    def print(self):
        print(self.parent[1:], self.rank[1:])


def simple_test1():
    st = DJSet()
    st.make_set(1)
    st.make_set(2)
    st.make_set(3)
    st.make_set(4)
    st.make_set(5)
    
    st.union(3, 5)
    st.print()
    st.union(2, 4)
    st.print()
    st.union(1, 4)
    st.print()
    st.union(5, 4)
    st.print()

if __name__ == "__main__":
    simple_test1()

    

