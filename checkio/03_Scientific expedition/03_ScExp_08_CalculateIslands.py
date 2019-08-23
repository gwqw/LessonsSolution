def find_island(land_map, x, y):
    #print("i,j to search= ", x,y)
    for j in range(y,len(land_map)):
        for i in range(0,len(land_map[0])):
            if land_map[j][i]: return i,j
    return -1,-1

def calc_area(land_map, x,y):
    MAX_X = len(land_map[0])-1
    MAX_Y = len(land_map)-1
    area = 1
    land_map[y][x] = 0 # zero if we count this square
    # move right
    if x < MAX_X and land_map[y][x+1]:
        area += calc_area(land_map, x+1, y)
    # move left
    if x > 0 and land_map[y][x-1]:
        area += calc_area(land_map, x-1, y)        
    # move down
    if y < MAX_Y and land_map[y+1][x]:
        area += calc_area(land_map, x, y+1)
    # move up
    if y > 0 and land_map[y-1][x]:
        area += calc_area(land_map, x, y-1)
    #move right and down
    if x < MAX_X and y < MAX_Y and land_map[y+1][x+1]:
        area += calc_area(land_map, x+1, y+1)
    #move left and down
    if x > 0 and y < MAX_Y and land_map[y+1][x-1]:
        area += calc_area(land_map, x-1, y+1)
    #move right and up
    if x < MAX_X and y > 0 and land_map[y-1][x+1]:
        area += calc_area(land_map, x+1, y-1)
    #move left and down
    if x > 0 and y > 0 and land_map[y-1][x-1]:
        area += calc_area(land_map, x-1, y-1)
    return area        

def checkio(land_map):
    print("")
    i,j = 0,0
    areas = []
    while True:
        area = 0
        # find point
        i,j = find_island(land_map, i,j)
        print("i, j= ", i, j)
        # if it is not founded
        if i == -1: break
        # find area of the founded island
        area += calc_area(land_map, i,j)
        areas.append(area)
        print("area= ", area)
        #print("land_map= ", land_map)
    areas.sort()
    print("areas= ", areas)
    return areas

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
