def onlyBrackets(s):
    l = list(filter((lambda x: x == '(' or x == ')' or x=='[' or x==']' or x=='{' or x=='}'),
           s))
    return ''.join(l)

def back_symbol(c):
    if c == '(': return ')'
    if c == '[': return ']'
    if c == '{': return '}'
    return 'l'

def check_expr(s):
    print(s)
    if not s: return True
    f = s[0]
    b = back_symbol(f)
    cnt = 1
    ns = ""
    for c in s[1:]:
        if c == f: cnt += 1
        elif c == b: cnt -=1
        if cnt == 0: break
        ns += c
    if cnt != 0: return False
    print("ns: ", ns)
    print("rest_str: ", s[len(ns)+2:])
    res = check_expr(ns)
    res = res and check_expr(s[len(ns)+2:])
    return res        

def checkio(expression):
    print("expression: ", expression)
    expression = onlyBrackets(expression)
    return check_expr(expression)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
