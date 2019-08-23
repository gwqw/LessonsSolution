def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    res = ""
    for ph in phrases:
        while True:
            i = ph.find("right")
            if i == -1: break
            ph = ph[:i] + "left" + ph[i+5:]
        res += ph + ','
    if res[-1] == ',': res = res[:-1]
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
