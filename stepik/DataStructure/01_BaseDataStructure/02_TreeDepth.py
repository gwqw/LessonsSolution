"""
    Tree height.
    Tree structure: parent_0, ..., parent_i, ..., parent_n-1
    where parent_i -- parent of i-th vertex
    Input:  n <- number of vertexes
            parent_0, ... <- tree structure
            root: parent = -1
            1 <= n <= 10^5
    Ex.1:
    5
    4 -1 4 1 1
    out:3

    Ex.2
    5
    -1 0 4 0 3
    out:4
"""

import sys

def parent_to_daughter_converter(parent_list):
    children_list = [None] * len(parent_list)
    for i,p in enumerate(parent_list):
        if p == -1: continue
        if children_list[p]:
            children_list[p].append(i)
        else:
            children_list[p] = [i]
    return children_list

class Tree:
    def __init__(self, value, parent, children):
        self.value = value
        self.parent = parent
        self.children = children

    def __str__(self):
        return "%d" % (self.value)

    @staticmethod
    def getTree(parent_rec):
        children_rec = parent_to_daughter_converter(parent_rec)
        value = parent_rec.index(-1)
        return Tree.getTreeInternal(children_rec, value, None)

    @staticmethod
    def getTreeInternal(daughter_rec, value, parent):
        # get root:
        children = daughter_rec[value]
        root = Tree(value, parent, [])
        if children:
            for ch in children:
                root.children.append(
                    Tree.getTreeInternal(daughter_rec, ch, root))
        return root
            
def HeightTree(tree):
    height = 1
    for ch in tree.children:
        height = max(height, 1+HeightTree(ch))
    return height

def PrintTree(tree):
    print(tree)
    for ch in tree.children:
        PrintTree(ch)

def str_to_parent_list(p_str):
    return [int(s) for s in p_str.split()]  

def test_ex():
    # example 1
    parent_list = str_to_parent_list("4 -1 4 1 1")
    assert(parent_list == [4, -1, 4, 1, 1])
    tree = Tree.getTree(parent_list)
    height = HeightTree(tree)
    assert(height == 3)
    # example 2
    parent_list = str_to_parent_list("-1 0 4 0 3")
    tree = Tree.getTree(parent_list)
    height = HeightTree(tree)
    assert(height == 4)
    # example 3
    parent_list = str_to_parent_list("9 7 5 5 2 9 9 9 2 -1")
    tree = Tree.getTree(parent_list)
    height = HeightTree(tree)
    assert(height == 4)
    # example 4
    parent_list = str_to_parent_list("-1")
    tree = Tree.getTree(parent_list)
    height = HeightTree(tree)
    assert(height == 1)

if __name__ == "__main__":
    test_ex()
    sys.setrecursionlimit(20000)
    input()
    tree = Tree.getTree(str_to_parent_list(input()))
    print(HeightTree(tree))
