# check if nums differs only by one digit
def isOneDiff(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    diffcount = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]: diffcount += 1
        if diffcount > 1: return False
    return (diffcount == 1)    

# find next nums in list
def findnext(numbers):
    first_num = numbers[0]
    next_nums = []
    for n in numbers[1:]:
        if isOneDiff(n, first_num):
            next_nums.append(n)
    return next_nums

# move next number to second position
def regroupList(numbers, snum):
    i = numbers.index(snum)
    reslst = numbers[:]
    n = reslst[i]
    reslst[i] = reslst[1]
    reslst[1] = n
    return reslst

# construct all trees
def constrTree(numbers):
    #print("inp_nums= ", numbers)
    res_tree = []
    isFinal = len(numbers) == 2
    finalNum = numbers[-1]
    # find next and form tree
    next_nums = findnext(numbers)
    #print("next_nums= ", next_nums)
    for n in next_nums:
        if n == finalNum:
            #print("find final")
            res_tree.append([numbers[0], n])
            break
        elif not isFinal:
            lst = regroupList(numbers, n)
            tmptree = constrTree(lst[1:])
            for t in tmptree:
                t.insert(0, numbers[0])
                res_tree.append(t)
    return res_tree

# find the shortest tree
def findShortest(trees):
    short_len = 100000
    short_tree = []
    for t in trees:
        if len(t) < short_len:
            short_len = len(t)
            short_tree = t
    return short_tree
    
def checkio(numbers):
    print("input_tree= ", numbers)
    res_trees = constrTree(numbers)
    print("res_trees= ", res_trees)
    short_tree = findShortest(res_trees)
    print("short_tree= ", short_tree)
    return short_tree

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
