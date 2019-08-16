"""
    Queue with priority
    Первая строка входа содержит число операций 1≤n≤105.
    Каждая из последующих n строк задают операцию одного из следующих двух типов:
    Insert x, 0 <= x <= 10^9 <- int
    ExtractMax
"""


class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, key):
        self.data.append(key)
        self.siftUp(len(self.data)-1)
        #self.print_tree()

    def extractMax(self):
        assert len(self.data) > 0
        res = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.siftDown(0)
        #self.print_tree()
        return res

    def siftUp(self, idx):
        while (idx-1) // 2 >= 0:
            jp = (idx-1) // 2
            if self.data[idx] > self.data[jp]:
                self.data[idx], self.data[jp] = self.data[jp], self.data[idx]
                idx = jp
            else:
                break

    def siftDown(self, idx):
        while 2*idx+1 < len(self.data):
            j = idx
            if self.data[2*idx+1] > self.data[j]:
                j = 2*idx+1
            if 2*idx+2 < len(self.data) and self.data[2*idx+2] > self.data[j]:
                j = 2*idx+2
            if idx == j:
                break
            self.data[idx], self.data[j] = self.data[j], self.data[idx]
            idx = j

    def clear(self):
        self.data.clear()

    def print_tree(self):
        print("Tree:")
        for v in self.data:
            print(v, end= " ")
        print("")

if __name__ == "__main__":
    #testHeap = MaxHeap()
    #operation_list = [("Insert")]
    n = int(input())
    operation_list = []
    for i in range(n):
        words = input().split()
        operation = words[0]
        count = 0
        if operation == "Insert":
            count = int(words[1])
            operation_list.append((operation, count))
        else:
            operation_list.append((operation, 0))
            
    heap = MaxHeap()
    for op in operation_list:
        if op[0] == "Insert":
            heap.insert(op[1])
        elif op[0] == "ExtractMax":
            print(heap.extractMax())
        else:
            print("Unknown operation")
