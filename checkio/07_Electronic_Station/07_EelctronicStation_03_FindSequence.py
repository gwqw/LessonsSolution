def obtain_cols(M):
    cols = []
    for i in range(len(M[0])):
        col = [row[i] for row in M]
        cols.append(col)
    return cols

def obtain_diag_list(M):
    diags = []
    N = len(M)
    for i in range(N):
        diag = []
        for j in range(i+1):
            diag.append(M[i-j][j])
        diags.append(diag)
    for i in range(1, N):
        diag = []
        for j in range(0, N-i):
            diag.append(M[N-j-1][i+j])    
        diags.append(diag)
    return diags

def obtain_main_diag_list(M):
    diags = []
    N = len(M)
    for i in range(N):
        diag = []
        for j in range(0,i+1):
            diag.append(M[j][N-1-i+j])
        diags.append(diag)

    for i in range(1,N):
        diag = []
        for j in range(N-i):
            diag.append(M[i+j][j])
        diags.append(diag)
    return diags

def count_in_lines(matrix):
    max_length = 1
    length = 1
    for l in matrix:
        if length > max_length: max_length = length
        length = 1
        cs = l[0]
        for i in l[1:]:
            if i == cs:
                length += 1
            else:
                cs = i
                if length > max_length: max_length = length
                length = 1
    if length > max_length: max_length = length
    return max_length


def checkio(matrix):
    max_length = 0
    # count in rows
    max_length = count_in_lines(matrix)
    print("Horiz: ", max_length)
    if max_length >= 4: return True
    # count in cols
    cols = obtain_cols(matrix)
    max_length = count_in_lines(cols)
    print("Vert: ", max_length)
    if max_length >= 4: return True
    # diagonal
    diags = obtain_diag_list(matrix)
    max_length = count_in_lines(diags)
    print("Diags: ", max_length)
    if max_length >= 4: return True
    # diagonal2
    diags = obtain_main_diag_list(matrix)
    max_length = count_in_lines(diags)
    print("Diags: ", max_length)
    if max_length >= 4: return True
    # nothing
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
