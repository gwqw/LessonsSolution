operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y,
              'mod': lambda x, y: x % y,
              'pow': lambda x, y: x ** y,
              'div': lambda x, y: x // y,
              }


if __name__ == "__main__":
    x, y = float(input()), float(input())
    c = input()
    if (c == '/' or c == "div" or c == 'mod') and y == 0:
        print("Деление на 0!")
    else:
        op = operations[c]
        print(op(x, y))
    
    
