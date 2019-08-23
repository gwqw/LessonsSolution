def checkio(number):
    print("")
    print("init food= ", number)
    food = number
    feed = 0
    i = 1
    while food:
        print("pidgeons= ", feed)
        print("pidgeons flew= ", i)
        print("food left= ", food)
        # food ends
        if feed + i >= food:
            feed += (food - feed) if food > feed else 0
            print("feeded= ", feed)
            return feed

        # feed some pidgeons
        feed += i
        food -= feed
        # new pigeons flew
        i += 1
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
