OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def conjuction(x, y):
    return int(x and y)

def disjunction(x, y):
    return int(x or y)

def implication(x, y):
    return int((not x) or y)

def exclusive(x, y):
    return (x != y)

def equivalence(x, y):
    return int(x == y)

def boolean(x, y, operation):
    if operation == "conjunction":
        return conjuction(x, y)
    elif operation == "disjunction":
        return disjunction(x, y)
    elif operation == "implication":
        return implication(x, y)
    elif operation == "exclusive":
        return exclusive(x, y)
    elif operation == "equivalence":
        return equivalence(x, y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
