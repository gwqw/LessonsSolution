def shrink_2_max(d):
    # find max letter count
    max_v = 0
    for k,v in d.items():
        if v > max_v: max_v = v

    # add only letter with max count
    letters = []
    for k,v in d.items():
        if v == max_v:
            letters.append(k)

    # sort alpabetial
    letters.sort()

    return(letters[0])   
        

def checkio(text):
    # add all symbols to dictionary
    d = {}
    for i in text.lower():
        if not i.isalpha(): continue
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    #print(d)

    # find sorted max
    ch = shrink_2_max(d)
    #print(ch)
    return ch


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
