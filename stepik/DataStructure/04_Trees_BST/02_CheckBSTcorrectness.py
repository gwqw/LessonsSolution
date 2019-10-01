"""
    Is binary search tree correct
    Input: # the same as in previous task
    n
    key_i, left_i, right_i
    Output:
    CORRECT or INCORRECT

    Ex.1
    3
    2 1 2
    1 -1 -1
    3 -1 -1
    out: CORRECT
"""

import sys

CORRECT = "CORRECT"
INCORRECT = "INCORRECT"


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, n):
        self.data = [None] * n
        self.idx = 0

    def add_node(self, key, left, right):
        self.data[self.idx] = Node(key, left, right)
        self.idx += 1

def in_order_lst(tree, idx):
    output = []
    if tree.data[idx].left != -1:
        output.extend(in_order_lst(tree, tree.data[idx].left))
    output.append(tree.data[idx].key)
    if tree.data[idx].right != -1:
        output.extend(in_order_lst(tree, tree.data[idx].right))
    return output

def is_correct(tree):
    order_lst = in_order_lst(tree, 0)
    return sorted(order_lst) == order_lst     

def test_example():
    # example 1
    tree = BinarySearchTree(3)
    tree.add_node(2, 1, 2)
    tree.add_node(1, -1, -1)
    tree.add_node(3, -1, -1)
    assert(is_correct(tree))

    # example 2
    tree = BinarySearchTree(5)
    tree.add_node(1, -1, 1)
    tree.add_node(2, -1, 2)
    tree.add_node(3, -1, 3)
    tree.add_node(4, -1, 4)
    tree.add_node(5, -1, -1)
    assert(is_correct(tree))

    # example 2_2
    tree = BinarySearchTree(5)
    tree.add_node(5, 1, -1)
    tree.add_node(4, 2, -1)
    tree.add_node(3, 3, -1)
    tree.add_node(2, 4, -1)
    tree.add_node(1, -1, -1)
    assert(is_correct(tree))

    # example 3
    tree = BinarySearchTree(7)
    tree.add_node(4, 1, 2)
    tree.add_node(2, 3, 4)
    tree.add_node(6, 5, 6)
    tree.add_node(1, -1, -1)
    tree.add_node(3, -1, -1)
    tree.add_node(5, -1, -1)
    tree.add_node(7, -1, -1)
    assert(is_correct(tree))

    # example 4
    tree = BinarySearchTree(4)
    tree.add_node(4, 1, -1)
    tree.add_node(2, 2, 3)
    tree.add_node(1, -1, -1)
    tree.add_node(5, -1, -1)
    assert(not is_correct(tree))
    

if __name__ == "__main__":
    test_example()
    n = int(input())
    sys.setrecursionlimit(20000)
    tree = BinarySearchTree(n)
    reader = (s.split() for s in sys.stdin)
    i = 0
    # fill tree
    if n:
        for words in reader:
            key, left, right = (int(s) for s in words)
            tree.add_node(key, left, right)
            i += 1
            if i == n: break
        if is_correct(tree):
            print(CORRECT)
        else:
            print(INCORRECT)
    else:
        print(CORRECT)
