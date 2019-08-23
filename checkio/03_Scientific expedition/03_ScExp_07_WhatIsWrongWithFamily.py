# solution is expand all 'path' of the tree to lines


def is_family_b(tree):
    print("tree= ", tree)
    lines = []
    lines.append(tree[0])
    ci = 0
    is_found = True
    for i in tree[1:]:
        if not is_found:
            print("False: not found")
            return False
        print('i= ', i)
        is_found = False
        for l in lines:
            print(l)
            if i[1] in l:
                print("False: Already exist")
                return False
            if i[0] in l:
                is_found = True
                if i[0] == l[-1]:
                    l.append(i[1])
                    print("lines= ", lines)
                else:
                    lines.append(i)
                    print("lines= ", lines)
                    break
    if not is_found:
        print("False: not found")
        return False
            
    print("res_lines= ", lines)
    return True

def check_intersection(res_lines, el):
    for lines in res_lines:
        if el in lines: return True
    return False

def get_next_element(tree, lines):
    if len(lines) == 0:
        return tree[0]
    for b in tree:
        # find children
        if b[0] in lines[0] and not check_intersection(lines, b[1]):
            return b
        elif b[0] in lines[0]:
            return None
        #find fathers
        elif b[1] == lines[0][0] and not check_intersection(lines, b[0]):
            return b
        elif b[1] == lines[0][0]:
            return None
    return None

def is_family(tree):
    print("")
    print("tree= ", tree)
    res_lines = []
    lines = []
    while len(tree) > 0:
        # obtain first element for line
        b = get_next_element(tree, res_lines)
        print("first= ", b)
        if not b:
            print("False: there are no good next(first)")
            return False
        lines.append(b[0])
        lines.append(b[1])
        tree.remove(b)
        print("init line= ", lines)
        # find all children line
        is_end = False
        while not is_end:
            # try to find next element (child)
            for b in tree:
                if lines[-1] == b[0]:
                    if b[1] in lines:
                        print("False: cycled by end")
                        return False
                    if check_intersection(res_lines, b[1]):
                        print("False: lines intersection (end)")
                        return False
                    lines.append(b[1])
                    tree.remove(b)
                    break
            else:
                is_end = True
        print("line(end)=", lines)
        # find possible father
        is_end = False        
        while not is_end:
            # try to find parent
            for b in tree:
                if lines[0] == b[1]:
                    if b[0] in lines:
                        print("False: cycled in the begin")
                        return False
                    if check_intersection(res_lines, b[0]):
                        print("False: lines intersection (begin)")
                        return False
                    lines.insert(0, b[0])
                    tree.remove(b)
                    break
            else:
                is_end = True
        print("line(begin)=", lines)
        res_lines.append(lines)
        lines = []
        print("res_lines", res_lines)
        print("end_of_tree", tree)
    return True

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
      ["Logan","Mike"],
      ["Alexander","Jack"],
      ["Jack","Logan"]
    ]) == True, 'Revert family tree'
    assert is_family([
     ["Logan","William"],
     ["William","Jack"],
     ["Jack","Mike"],
     ["Mike","Alexander"]
    ]) == True, 'Long line'
    assert is_family([
     ["Logan","William"],
     ["Mike","Alexander"],
     ["William","Alexander"]
    ]) == False, 'Who\'s your daddy'
    print("Looks like you know everything. It is time for 'Check'!")
