def completely_empty(val):
    print("val= ", val)
    try:
        iterator = iter(val)
    except TypeError:
        # not iterable
        print("False: is not iterable")
        return False

    # iterable and empty
    if not val:
        print("True: empty iterable")
        return True
    
    # iterable and contains smth
    for i in val:
        res = completely_empty(i)
        if not res:
            print("False: iterable contains smth")
            return False
    print("True: There aro no anything in iterable")
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    assert completely_empty([iter(())]) == True, "iter"
    print('Done')
