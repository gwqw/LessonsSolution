"""
    Write in-order, pre-order and post-order go through binary search tree
    in-order:   v.left, v.key, v.right
    pre-order:  v.key, v.left, v.right
    post-order: v.left, v.right, v.key
    Input:
    n # number of vertexes, 0 -- root
    key_i left_i right_i # i-th vertex: left_i -- index of left son, -1 -- no son

    Out:
    in-order
    pre-order
    post-order

    1 <= n <= 1e5, 0 <= key <= 1e9

    Ex.1:
    5
    4 1 2
    2 3 4
    5 -1 -1
    1 -1 -1
    3 -1 -1
    out:
    1 2 3 4 5
    4 2 1 3 5
    1 3 2 5 4
"""

import sys

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

def pre_order_lst(tree, idx):
    output = []
    output.append(tree.data[idx].key)
    if tree.data[idx].left != -1:
        output.extend(pre_order_lst(tree, tree.data[idx].left))
    if tree.data[idx].right != -1:
        output.extend(pre_order_lst(tree, tree.data[idx].right))
    return output

def post_order_lst(tree, idx):
    output = []
    if tree.data[idx].left != -1:
        output.extend(post_order_lst(tree, tree.data[idx].left))    
    if tree.data[idx].right != -1:
        output.extend(post_order_lst(tree, tree.data[idx].right))
    output.append(tree.data[idx].key)
    return output

def test_example():
    # example 1
    tree = BinarySearchTree(5)
    tree.add_node(4, 1, 2)
    tree.add_node(2, 3, 4)
    tree.add_node(5, -1, -1)
    tree.add_node(1, -1, -1)
    tree.add_node(3, -1, -1)
    assert(in_order_lst(tree, 0) == [1, 2, 3, 4, 5])
    assert(pre_order_lst(tree, 0) == [4, 2, 1, 3, 5])
    assert(post_order_lst(tree, 0) == [1, 3, 2, 5, 4])

    # example 2
    tree = BinarySearchTree(10)
    tree.add_node(0, 7, 2)
    tree.add_node(10, -1, -1)
    tree.add_node(20, -1, 6)
    tree.add_node(30, 8, 9)
    tree.add_node(40, 3, -1)
    tree.add_node(50, -1, -1)
    tree.add_node(60, 1, -1)
    tree.add_node(70, 5, 4)
    tree.add_node(80, -1, -1)
    tree.add_node(90, -1, -1)
    assert(in_order_lst(tree, 0) == [50, 70, 80, 30, 90, 40, 0, 20, 10, 60])
    assert(pre_order_lst(tree, 0) == [0, 70, 50, 40, 30, 80, 90, 20, 60, 10])
    assert(post_order_lst(tree, 0) == [50, 80, 90, 30, 40, 70, 10, 60, 20, 0])

if __name__ == "__main__":
    test_example()
    n = int(input())
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
    output = in_order_lst(tree, 0)
    for o in output:
        print(o, end = " ")
    print()
    output = pre_order_lst(tree, 0)
    for o in output:
        print(o, end = " ")
    print()
    output = post_order_lst(tree, 0)
    for o in output:
        print(o, end = " ")
    print()
        
