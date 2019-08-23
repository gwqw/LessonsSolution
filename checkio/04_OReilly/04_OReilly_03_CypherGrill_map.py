MAT_SIZE = 4

def rotate_matrix(mat):
    res_mat = []
    for i in range(MAT_SIZE):
        res_mat.append('')
        for j in range(MAT_SIZE):
            res_mat[i] += mat[MAT_SIZE-1-j][i]
    return res_mat

def obtain_side_pass(cipher_grille, pass_mat):
    res = ''
    for i in range(MAT_SIZE):
        for j in range(MAT_SIZE):
            if cipher_grille[i][j] == 'X':
                res += pass_mat[i][j]
    return res
    
def recall_password(cipher_grille, ciphered_password):
    # 0 gr
    pas = obtain_side_pass(cipher_grille, ciphered_password)
    # 90 gr
    cipher_grille = rotate_matrix(cipher_grille)
    pas += obtain_side_pass(cipher_grille, ciphered_password)
    # 180 gr
    cipher_grille = rotate_matrix(cipher_grille)
    pas += obtain_side_pass(cipher_grille, ciphered_password)
    # 270 gr
    cipher_grille = rotate_matrix(cipher_grille)
    pas += obtain_side_pass(cipher_grille, ciphered_password)
    return pas

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
