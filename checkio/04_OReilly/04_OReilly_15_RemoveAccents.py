def checkio(in_string):
    "remove accents"
    import unicodedata
    res = unicodedata.normalize('NFD', in_string)
    res = res.encode('ascii', 'ignore')
    res = res.decode("utf-8")
    return res

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(u"préfèrent"))
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
