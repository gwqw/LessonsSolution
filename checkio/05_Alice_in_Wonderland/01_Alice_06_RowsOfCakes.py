INF = 1e10

def get_row(p1, p2):
    # y = a * x + b
    #print("p1, p2= ", p1, ", ", p2)
    if p2[0] - p1[0] != 0:
        a = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = p2[1] - a * p2[0]
    else:
        a = INF
        b = p1[0]
    #print("a, b= ", a, ", ", b)
    return [a, b]

def get_rows(points):
    # for every pair get row as line koeffs
    rows = []
    for i, p1 in enumerate(points[:-1]):
        for p2 in points[i+1:]:
            rows.append(get_row(p1, p2))
    rows.sort()
   # print(rows)
    # count lines with more than 2 points    
    cp = rows[0]
    counts = 0
    lines_count = 0
    for i in range(1,len(rows)):
        if rows[i] == cp:
            counts += 1
            if i == len(rows)-1:
                lines_count += 1
                #print("a, bf= ", cp, ", ", rows[i])
        elif counts > 0:
            #print("a, b= ", cp)
            lines_count += 1
            cp = rows[i]
            counts = 0            
        else:
            cp = rows[i]
            counts = 0
    #print(lines_count)
    return lines_count        

def checkio(cakes):
    return get_rows(cakes)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
