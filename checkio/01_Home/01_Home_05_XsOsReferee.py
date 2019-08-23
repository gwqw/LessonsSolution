def checkio(game_result):
    for i in range(0,len(game_result)):
        # horizontal
        if game_result[i] == 'XXX': return 'X'
        elif game_result[i] == 'OOO': return 'O'
        # vertical
        s = ''
        for j in range(0,len(game_result)):
            s += game_result[j][i]
        if s == 'XXX': return 'X'
        elif s == 'OOO': return 'O'
        
    # diagonals
    s = ''
    s1 = ''
    for i in range(0,len(game_result)):
        s += game_result[i][i]
        s1 += game_result[len(game_result)-i-1][i]
    if s == 'XXX' or s1 == 'XXX': return 'X'
    elif s == 'OOO' or s1 == 'OOO': return 'O'
    # draw        
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
