def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    res_dic = {}
    for s in data:
        if s in res_dic:
            res_dic[s] += 1
        else:
            res_dic[s] = 1
    max_v = 0
    res = ''
    for k,v in res_dic.items():
        if v > max_v:
            max_v = v
            res = k
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
