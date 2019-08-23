def findMaxRowsLen(rows):
    max_len = 0
    for row in rows:
        if len(row) > max_len:
            max_len = len(row)
    return max_len

def findWordInRows(word, text):
    rows = text.split('\n')
    #print(rows)
    for i,row in enumerate(rows):
        tpos = row.find(word)
        if tpos != -1:
            print([i+1, tpos+1, i+1, tpos+len(word)])
            return [i+1, tpos+1, i+1, tpos+len(word)]

def findWordInCols(word, text):
    rows = text.split('\n')
    max_len = findMaxRowsLen(rows)
    # rows to equal length
    for i in range(len(rows)):
        if len(rows[i]) < max_len:
            rows[i] += ' ' * (max_len - len(rows[i]))
    # obtain columns
    cols = []
    for c in range(max_len):
        cur_col = []
        for row in rows:
            cur_col.append(row[c])
        #cur_col = [row[c] for row in rows]
        cols.append(''.join(cur_col))
    # find value
    for i,col in enumerate(cols):
        tpos = col.find(word)
        if tpos != -1:
            print([tpos+1, i+1, tpos+len(word), i+1])
            return [tpos+1, i+1, tpos+len(word), i+1]
    return []

def checkio(text, word):
    # convert text to lower case and remove spaces
    text = text.lower()
    tmp = text.split(' ')
    text = ''.join(tmp)
    print()
    print(word)
    # find word in rows
    if word in text:
        print(f"word {word} is in rows")
        return findWordInRows(word, text)
    else:
        print(f"try to find word {word} in columns")
        return findWordInCols(word, text)
    print("algorythm bullshit")
    return [1, 1, 1, 4]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
