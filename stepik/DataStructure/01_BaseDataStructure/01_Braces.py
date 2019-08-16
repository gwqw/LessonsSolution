"""
Braces in the code
Check if braces are correct
Input: program code with braces: there can be letters, numbers and (), [], {}
Output: If braces are correct -- "Success"
        else -- return index (from 1) of the first close brace for which there are no open
        or index of first open brace for which there are no open
Restrictions: input lenght (n): 1 <= n <= 10^5

Example 1:
{}[]
Success

Example 2:
{()}
Success

Example 3
{[]}()
Success

Example 4:
{
1

Example 5:
foo(bar)
Success

Example 6:
foo(bar[i);
10
"""

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

class Item:
    def __init__(self, idx, char):
        self.char = char
        self.idx = idx

braces_map = {'(':')', '[':']', '{':'}'}

def is_correct_string(string):
    stack = Stack()
    for i,c in enumerate(string):
        if c in "([{":
            stack.push(Item(i,c))
        elif c in ")]}" and not stack.is_empty():
            item = stack.pop()
            if braces_map[item.char] != c:
                return i+1
        elif c in ")]}" and stack.is_empty():
            return i+1
    if stack.is_empty():
        return "Success"
    else:
        return stack.pop().idx+1

def test_examples():
    assert(is_correct_string("{}[]") == "Success")
    assert(is_correct_string("{()}") == "Success")
    assert(is_correct_string("{[]}()") == "Success")
    assert(is_correct_string("{") == 1)
    assert(is_correct_string("foo(bar)") == "Success")
    assert(is_correct_string("foo(bar[i);") == 10)
    

if __name__ == "__main__":
    test_examples()
    print(is_correct_string(input()))
