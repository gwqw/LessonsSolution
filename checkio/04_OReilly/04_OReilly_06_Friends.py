class Friends:
    def __init__(self, connections):
        self.connections = []
        self.connections.extend(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        self.connections.append(connection)
        return True

    def remove(self, connection):
        if not connection in self.connections:
            return False
        self.connections.remove(connection)
        return True

    def names(self):
        res = set()
        for c in self.connections:
            for i in c:
                res.add(i)
        return res
    
    def connected(self, name):
        res = []
        for c in self.connections:
            if name in c:
                print("c= ", c)
                a = set()
                a.add(name)
                print("a= ", a)
                c = c - a
                print("c_diff= ", c)
                c = c.pop()
                print("c_str= ", c)
                res.append(c)
                print("res= ", res)
        return set(res)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    assert f.connected("nikola") == {"sophia"}, "Ahem"
