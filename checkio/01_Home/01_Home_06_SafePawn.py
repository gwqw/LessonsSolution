def safe_pawns(pawns):
    guarded = 0
    rows = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    for p in pawns:
        # calc 2 pos for defend pawn
        i1 = rows.index(p[0]) - 1
        i2 = rows.index(p[0]) + 1
        if i1 >= 0: pos1 = rows[i1] + str(int(p[1])-1)
        else: pos1 = None
        if i2 < len(rows): pos2 = rows[i2] + str(int(p[1])-1)
        else: pos2 = None
        #check for guard (existance)
        if (pos1 and (pos1 in pawns) or pos2 and (pos2 in pawns)): guarded += 1

    return guarded

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
