"""
    Stack with minimum. Methods: push, pop, max
    Input: q -- all queries
        push v, pop or max
        1 <= q <= 400'000, 0 <= v <= 1e5

    Ex.1:
    3
    push 1
    push 7
    pop
    Out: # no max queries

    Ex.2:
    5
    push 2
    push 1
    max
    pop
    max
    Out
    2
    2

    Ex.3:
    6
    push 7
    push 1
    push 7
    max
    pop
    max
    out:
    7
    7

    Ex.4:
    5
    push 1
    push 2
    max
    pop
    max
    Out:
    2
    1

    Ex.5:
    10
    push 2
    push 3
    push 9
    push 7
    push 2
    max
    max
    max
    pop
    max
    Out:
    9
    9
    9
    9
"""

import sys

class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return (self.items == [])


class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()
        self.max_value = -1

    def push(self, v):
        self.stack.push(v)
        self.max_stack.push(max(v, self.max_value))
        self.max_value = max(v, self.max_value)

    def pop(self):
        self.stack.pop()
        self.max_stack.pop()
        if not self.max_stack.is_empty():
            self.max_value = self.max_stack.top()
        else:
            self.max_value = -1

    def max(self):
        return self.max_value


def test_example():
    # example 1
    stack = MaxStack()
    stack.push(2)
    stack.push(1)
    assert(stack.max() == 2)
    stack.pop()
    assert(stack.max() == 2)

    # example 2
    stack = MaxStack()
    stack.push(7)
    stack.push(1)
    stack.push(7)
    assert(stack.max() == 7)
    stack.pop()
    assert(stack.max() == 7)

    # example 3
    stack = MaxStack()
    stack.push(1)
    stack.push(2)
    assert(stack.max() == 2)
    stack.pop()
    assert(stack.max() == 1)

    # example 3
    stack = MaxStack()
    stack.push(2)
    stack.push(3)
    stack.push(9)
    stack.push(7)
    stack.push(2)
    assert(stack.max() == 9)
    assert(stack.max() == 9)
    assert(stack.max() == 9)
    stack.pop()
    assert(stack.max() == 9)

if __name__ == "__main__":
    test_example()
    n = int(input())
    stack = MaxStack()
    reader = (line.split() for line in sys.stdin)
    i = 0
    for words in reader:
        if len(words) == 2 and words[0] == "push":
            stack.push(int(words[1]))
        elif len(words) == 1 and words[0] == "pop":
            stack.pop()
        elif len(words) == 1 and words[0] == "max":
            print(stack.max())
        i += 1
        if i == n: break
        
        
        

