def sun_angle(time):
    h,m = time.split(':')
    x = int(h)*60 + int(m)
    if x < 6*60 or x > 18*60:
        return "I don't see the sun!"
    return 180/(12*60) * (x - 6*60)    

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
