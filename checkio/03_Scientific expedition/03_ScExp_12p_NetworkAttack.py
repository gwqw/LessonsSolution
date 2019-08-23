INF = 100

def recalc_inf_time(matrix, pc, inf_time, infected, ct):
    is_infected = False
    for i in range(len(matrix)):
        if i == pc: continue
        if matrix[pc][i] and not infected[i]:
            # trying to infect
            if inf_time[i] == INF:
                print(f"\ttrying to infect {i} from {pc}")
                inf_time[i] = ct + matrix[i][i]
                print(f"\ttime to infection: {inf_time[i]}")
            # check in already infected
            elif inf_time[i] <= ct:
                infected[i] = True
                print("\t", i, " - infected!!!")
                is_infected = True
    return is_infected

def calc_min_time(inf_time, infected, ct):
    min_time_leap = INF
    for i in range(len(inf_time)):
        if not infected[i]:
            print(f"time to {i} infection is {inf_time[i] - ct}")
        if not infected[i] and inf_time[i] - ct < min_time_leap:
            if inf_time[i] != INF:
                min_time_leap = inf_time[i] - ct
    return min_time_leap

def capture(matrix):
    print("")
    inf_time = [INF for i in range(len(matrix))]
    infected = [False for i in range(len(matrix))]
    infected[0] = True
    ct = 0
    while not all(infected):
        print("current time= ", ct)
        print("infected= ", infected)        
        min_time = INF
        while True:
            is_infect = False
            for i in range(len(infected)):
                if infected[i]:
                    print(f"check {i} infections")
                    is_infect = is_infect or recalc_inf_time(matrix, i, inf_time, infected, ct)
            if not is_infect: break
        if all(infected):
            print("res_time= ", ct)
            return ct
        min_time = calc_min_time(inf_time, infected, ct)
        print("time to next infection= ", min_time)
        if (min_time == INF or min_time == 0):
            print("infected= ", infected)
            print("Something goes wrong")
            return INF
        print("leap time= ", min_time)
        if not all(infected):
            ct += min_time 
    return ct

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
    assert capture([[0,1,0],
                    [1,9,1],
                    [0,1,9]]) == 18, "Test1"
    assert capture([[0,0,0,0,1,0,0],
                    [0,4,0,1,1,0,1],
                    [0,0,1,0,0,1,1],
                    [0,1,0,3,0,0,1],
                    [1,1,0,0,1,0,0],
                    [0,0,1,0,0,5,1],
                    [0,1,1,1,0,1,2]]) == 12
