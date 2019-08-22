"""
    Set with numbers can treat requests:
        add_number, del_number, search_number, get_sum(from, to)
    Input:
    + i # add number f(i) (if it in set, so ignore)
    - i # delete number f(i) (if it does not in set, so ignore)
    ? i # check f(i) in set
    s l r # calc sum of all nums in [f(l), f(r)]
    f(x): if s -- result of last sum request, so f(x) = (x + s) % 1 000 000 001
    Ouput:
    Found or Not Found # for ?
    number # for sum
"""

