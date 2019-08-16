"""
    Find maximum in sliping size m in sequence of size n: A[1..n]
    Input:
    n (1 <= n <= 1e5)
    A[1..n]
    m: 1 <= m <= n
    Output: max in A[i..i+m-1] for i in [1, n-m+1] separatied with spaces

Ex.1:
8
2 7 3 1 5 2 6 2
4
out: 7 7 5 6 6

Ex.2:
3
2 1 5
1
out: 2 1 5

Ex.3:
3
2 3 9
3
out: 9

Algo:

    
"""

class Deque:
    def __init__(self, max_size, zero_value):
        assert(max_size > 0)
        self.data = [zero_value] * max_size
        self.size = 0
        self.front_ = 0
        self.back_ = 0
        self.max_size = max_size

    def push_back(self, value):
        assert(self.size < self.max_size)
        self.size += 1
        self.data[self.back_] = value
        self.back_ = (self.back_ + 1) % self.max_size        

    def pop_front(self):
        assert(self.size > 0)
        self.size -= 1
        value = self.data[self.front_]
        self.front_ = (self.front_ + 1) % self.max_size
        return value

    def pop_back(self):
        assert(self.size > 0)
        self.size -= 1
        self.back_ = (self.back_ - 1) % self.max_size
        value = self.data[self.back_]
        return value

    def front(self):
        assert(self.size > 0)
        return self.data[self.front_]

    def back(self):
        assert(self.size > 0)
        idx = (self.back_ - 1) % self.max_size
        return self.data[idx]

    def empty(self):
        return self.size == 0

    def get_list(self):
        if self.size == 0: return []
        if self.back_ > self.front_:
            return self.data[self.front_ : self.back_]
        else:
            return self.data[self.front_ : -1] + self.data[0 : self.back_]

    def __str__(self):
        if self.back_ > self.front_:
            return ", ".join([str(i) for i in self.data[self.front_ : self.back_]])
        else:
            return "back"
            
        

def insert_value_remove_smaller(deque, value):
    while not deque.empty() and deque.back() < value:
        deque.pop_back()
    deque.push_back(value)

def remove_left_value(deque, value):
    if not deque.empty() and deque.front() == value:
        deque.pop_front()

def get_maximums(a, m):
    deque = Deque(m, -1)
    n = len(a)
    output = []
    for i in range(m-1):
        insert_value_remove_smaller(deque, a[i])
        
    for i in range(m-1, n):
        insert_value_remove_smaller(deque, a[i])
        output.append(deque.front())    
        remove_left_value(deque, a[i-m+1])
    return output        

def test_example():
    assert(get_maximums([2, 7, 3, 1, 5, 2, 6, 2], 4) == [7, 7, 5, 6, 6])
    assert(get_maximums([2, 1, 5], 1) == [2, 1, 5])
    assert(get_maximums([2, 3, 9], 3) == [9])

if __name__ == "__main__":
    test_example()
    n = int(input())
    a = [int(s) for s in input().split()]
    m = int(input())
    output = get_maximums(a, m)
    for o in output:
        print(o, end = " ")
