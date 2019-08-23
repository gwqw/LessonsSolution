def getTriangularNums(N):
    reslst = [0]
    for i in range(1,N):
        reslst.append(reslst[-1] + i)
    return reslst

def findCloseMin(v, tlist):
    for i in range(len(tlist)):
        if v < tlist[i]: return i-1        

def checkio(number):
    #print(f"number = {number}")
    trianlst = getTriangularNums(100)
    minTrNum = findCloseMin(number, trianlst)
    if minTrNum == number: return number
    maxtrlen = 0
    maxreslst = []
    while minTrNum > 0:
        #print(f"minTrNum = {minTrNum}, trlist = {trianlst[minTrNum]}")
        trsum = 0
        reslst = []
        trlen = 0
        for i in range(minTrNum, -1, -1):
            trsum += trianlst[i]
            reslst.append(trianlst[i])
            trlen += 1
            #print(f"\trsum= {trsum}, reslst= {reslst}")
            if trsum == number and trlen > maxtrlen:
                maxtrlen = trlen
                maxreslst = reslst
                break
            if trsum > number: break
        minTrNum -= 1
    
    maxreslst.sort()
    #print(maxreslst)
    return maxreslst

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
