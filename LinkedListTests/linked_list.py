"""
    Test work with linked list
"""

class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        return not self.head

    def push(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        cur = self.head
        res = []
        while cur:
            res.append(str(cur))
            cur = cur.next
        return "->".join(res)

    def find(self, value):
        cur = self.head
        while cur:
            if value == cur.value: return cur
            cur = cur.next
        return None

    def find_before(self, value):
        cur = self.head
        if not cur: return None
        while cur.next:
            if cur.next.value == value: return cur
            cur = cur.next
        return None

    def insert(self, node, value):
        node.next = Node(value, node.next)

if __name__ == "__main__":
    ll = LinkedList()
    print("Is empty:", ll.empty())
    ll.push(1)
    print("Is empty:", ll.empty())
    ll.push(2)
    ll.push(3)
    ll.push(4)
    print(ll)
    nd = ll.find(3)
    if nd:
        print(3, "in list")
        print("insertion after 3")
        ll.insert(nd, 6)
        print(ll)
    nd = ll.find_before(3)
    if nd:
        print("insertion before 3")
        ll.insert(nd, 7)
        print(ll)
    nd = ll.find_before(4)
    if nd:
        print(4, "in list")
        
    
