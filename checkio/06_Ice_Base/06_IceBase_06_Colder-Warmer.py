def calc_area(steps):
    minX = minY = 0
    maxX = maxY = 9
    for i in range(1,len(steps)):
        if steps[i][0] == 2 and steps[i][1] == 2:
            continue
        if steps[i][0] > steps[i-1][0]:
            if steps[i][2] == 1 and minX < steps[i][0]:
                minX = steps[i][0]
            elif steps[i] == -1 and maxX > steps[i-1][0]:
                maxX = steps[i-1][0]
        elif steps[i][0] < steps[i-1][0]:
            if steps[i][2] == 1 and maxX > steps[i][0]:
                maxX = steps[i][0]
            elif steps[i][2] == -1 and minX < steps[i-1][0]:
                minX = steps[i-1][0]
        elif steps[i][1] > steps[i-1][1]:
            if steps[i][2] == 1 and minY < steps[i][1]:
                minY = steps[i][1]
            elif steps[i][2] == -1 and maxY > steps[i-1][1]:
                maxY = steps[i-1][1]
        elif steps[i][1] < steps[i-1][1]:
            if steps[i][2] == 1 and maxY > steps[i][1]:
                maxY = steps[i][1]
            elif steps[i][2] == -1 and minY < steps[i-1][1]:
                minY = steps[i-1][1]
    return [minX, maxX, minY, maxY]

def in_area(x, y, area):
    return x >= area[0] and x <= area[1] and y >= area[2] and y <= area[3]

def has_step(x, y, steps):
    for s in steps:
        if x == s[0] and y == s[1]:
            return True
    return False

def get_direction(steps):
    if steps[-1][0] > steps[-2][0]: return 0
    if steps[-1][0] < steps[-2][0]: return 1
    if steps[-1][1] > steps[-2][1]: return 2
    if steps[-1][1] < steps[-2][1]: return 3

def get_ave_area(area):
    x = (area[1] + area[0]) // 2
    y = (area[3] + area[2]) // 2
    return x,y

def checkio(steps):
    print(f"{len(steps)}steps: {steps}")
    if len(steps) == 1:
        if steps[0] != [5, 5, 0]:
            return 5, 5
        else:
            return 4, 5
    
    area = calc_area(steps)
    print("area: ", area)
    x = steps[-1][0]
    y = steps[-1][1]
    
    direction = get_direction(steps)
    if direction > 1:
        if in_area(x+1, y, area) and not has_step(x+1, y, steps):
            return x+1, y
        elif in_area(x-1, y, area) and not has_step(x-1, y, steps):
            return x-1, y
        elif in_area(x, y+1, area) and not has_step(x, y+1, steps):
            return x, y+1
        elif in_area(x, y-1, area) and not has_step(x, y-1, steps):
            return x, y-1
    if direction <= 1:
        if in_area(x, y+1, area) and not has_step(x, y+1, steps):
            return x, y+1
        elif in_area(x, y-1, area) and not has_step(x, y-1, steps):
            return x, y-1
        elif in_area(x+1, y, area) and not has_step(x+1, y, steps):
            return x+1, y
        elif in_area(x-1, y, area) and not has_step(x-1, y, steps):
            return x-1, y

    return get_ave_area(area)

if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from math import hypot
    MAX_STEP = 12
    #MAX_STEP = 24

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                print("You find it! ", row, ", ", col)
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
            distance = hypot(row - goal[0], col - goal[1])
            alteration = 0 if prev_distance == distance else (1 if prev_distance > distance else -1)
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
    #assert check_solution(checkio([[0,0,0],[2,2,1],[2,3,1],[3,3,1],[3,4,1],[4,4,1],[4,5,1],[5,5,1],[5,6,1],[6,6,1],[6,7,1],[7,7,1],[7,8,1]]), , "3rd example")
