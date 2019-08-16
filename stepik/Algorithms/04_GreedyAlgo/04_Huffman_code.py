"""
    H <- queue with priorities
    for i in range(n):
        insert(h, (i, F(i)))
    for k in range(n+1, 2n-1):
        (i, F(i)) <- extract_min(h)
        (j, F(j)) <- extract_min(h)
        Vertex(k, i, j)
        F[k] = F[i] + F[j]
        insert(h, (k, F(k)))
"""

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def print_recursive(self):
        print(self.data)
        if self.left:
            self.left.print_recursive()
        if self.right:
            self.right.print_recursive()

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def newNode(self, data):
        return Node(data, None, None)

    def print_tree(self):
        if self.root:
            self.root.print_recursive()

def get_freq_array(string):
    freq_arr = {}
    for c in string:
        if c in freq_arr:
            freq_arr[c] += 1
        else:
            freq_arr[c] = 1
    return freq_arr    
        

def pop_min_arr(arr):
    if len(arr) == 0: return None
    min_v = arr[0]
    min_i = 0
    for i in range(len(arr)):
        if arr[i].data[1] < min_v.data[1]:
            min_v = arr[i]
            min_i = i            
    return arr.pop(min_i)

def code_from_tree(node, code_map, code):
    # leaf
    if node.left == None and node.right == None:
        if code == "": code = "0"
        code_map[node.data[0]] = code
        return code_map
    # has left subtree
    if node.left != None:
        code_map = code_from_tree(node.left, code_map, code + '0')
    # has right sub tree
    if node.right != None:
        code_map = code_from_tree(node.right, code_map, code + '1')
    return code_map

def code_from_table(table, string):
    code = ""
    for c in string:
        code += table[c]
    return code

if __name__ == "__main__":
    #string = "a"
    string = input()
    
    input_arr = get_freq_array(string) 
    #print(input_arr)
    n = len(input_arr)
    tree = Tree()
    nodes = []
    # add leaves
    for k, v in input_arr.items():
        nodes.append(tree.newNode((k,v)) )
    tree.root = nodes[-1]
    # create Tree 
    for k in range(n, 2*n-1):
        n1 = pop_min_arr(nodes)
        n2 = pop_min_arr(nodes)
        #print("Step")
        #print(n1)
        #print(n2)
        if n1.left != None:
            n = Node(('', n1.data[1] + n2.data[1]), n2, n1)
        elif n2.left != None:
            n = Node(('', n1.data[1] + n2.data[1]), n1, n2)
        else:
            n = Node(('', n1.data[1] + n2.data[1]), n2, n1)
        tree.root = n
        nodes.append(n)
    # print tree
    #print("Tree")
    #tree.print_tree()

    #obtain shifr
    code_table = code_from_tree(tree.root, {}, "")
    #print("Table")
    #print(code_table)

    # obtain code
    code = code_from_table(code_table, string)
    #print(code)

    #output
    print(len(code_table), len(code))
    for k, v in code_table.items():
        print(k, v, sep = ": ")
    print(code)
    

    
