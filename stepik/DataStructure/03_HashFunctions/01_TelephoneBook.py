"""
    Telephone book.
    Commands: add number name; del number; find number
    Output: for find: if found -> name else -> not found
"""

import sys

NOT_FOUND = "not found"

class TelephoneBook:
    def __init__(self):
        self.book = dict()

    def add(self, number, name):
        self.book[number] = name

    def delete(self, number):
        if number in self.book:
            self.book.pop(number)

    def find(self, number):
        return self.book.get(number, NOT_FOUND)

def example1():
    # example1
    tb = TelephoneBook()
    tb.add(911, "police")
    tb.add(76213, "Mom")
    tb.add(17239, "Bob")
    assert(tb.find(76213) == "Mom")
    assert(tb.find(910) == NOT_FOUND)
    assert(tb.find(911) == "police")
    tb.delete(910)
    tb.delete(911)
    assert(tb.find(911) == NOT_FOUND)
    assert(tb.find(76213) == "Mom")
    tb.add(76213, "daddy")
    assert(tb.find(76213) == "daddy")

    # example2
    tb = TelephoneBook()
    assert(tb.find(3839442) == NOT_FOUND)
    tb.add(123456, "me")
    tb.add(0, "granny")
    assert(tb.find(0) == "granny")
    assert(tb.find(123456) == "me")
    tb.delete(0)
    tb.delete(0)
    assert(tb.find(0) == NOT_FOUND)
    

if __name__ == "__main__":
    example1()
    n = int(input())
    reader = (line.split() for line in sys.stdin)
    i = 0
    tb = TelephoneBook()
    output = []
    for words in reader:
        if words[0] == "add":
            tb.add(int(words[1]), words[2])
        elif words[0] == "del":
            tb.delete(int(words[1]))
        elif words[0] == "find":
            output.append(tb.find(int(words[1])))
        i += 1
        if i == n: break
        
    for o in output:
        print(o)
