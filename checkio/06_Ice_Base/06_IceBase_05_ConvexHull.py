import math

INF = 1e6

def findLeftBottomPoint(data):
    minP = data[0]
    for p in data[1:]:
        if p[0] < minP[0]: minP = p
        elif p[0] == minP[0] and p[1] < minP[1]: minP = p
    return data.index(minP)

def getVector(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1]]

def getCos(pPoint, iPoint, tPoint):
    #print(f"pPoint, iPoint, tPoint= {pPoint, iPoint, tPoint}")
    mod = lambda x,y: math.sqrt(x**2 + y**2)
    vecTo = getVector(pPoint, iPoint)
    vecFrom = getVector(iPoint, tPoint)
    modTo = mod(vecTo[0], vecTo[1])
    modFrom = mod(vecFrom[0], vecFrom[1])
    if modTo != 0 and modFrom != 0:
        cos_alpha = ((vecTo[0]*vecFrom[0] + vecTo[1]*vecFrom[1]) /
            (mod(vecTo[0], vecTo[1]) * mod(vecFrom[0], vecFrom[1])))
    else:
        return -2, modFrom
    return cos_alpha, modFrom

def fill_points(data, left, res_lst):
    if left not in res_lst: res_lst.append(left)

    # find points to check
    indices = list(range(len(data)))
    print("Found indices: ", indices)

    # find point with minimal angle
    iPoint = data[left]
    pPoint = data[left][:]
    pPoint[1] -= 1
    while True:
        max_cos = -2
        max_ind = 0
        min_dist = INF
        print("indices: ", indices)
        for i in indices:
            ccos, cdist = getCos(pPoint, iPoint, data[i])
            print(f"\tccos= {ccos}, cdist= {cdist}")
            if (ccos - max_cos) > 1e-4:
                max_ind, max_cos = i, ccos
                min_dist = cdist
            elif abs(ccos - max_cos) <= 1e-4 and cdist < min_dist:
                max_ind, max_cos = i, ccos
                min_dist = cdist
        print("found index with max cos: ", max_ind)
        if max_ind != left:
            res_lst.append(max_ind)
            pPoint = iPoint
            iPoint = data[max_ind]
            indices.remove(max_ind)
        else:
            break
        if not indices: break


def checkio(data):
    """list[list[int, int],] -> list[int,]
    Find the convex hull.
    """
    res_lst = []
    print("")
    print("test data: ", data)
    left = findLeftBottomPoint(data)
    print(f"Left point is {left}")
    fill_points(data, left, res_lst)
    print("result list: ", res_lst)
    return res_lst

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
    assert checkio([[2,5],[5,5],[5,2],[2,2]]) == [3, 0, 1, 2], "Third example"
    assert checkio([[7,4],[5,2],[4,7],[4,1],[3,6],[1,4]]) == [5,4,2,0,1,3], "Points is on line"
