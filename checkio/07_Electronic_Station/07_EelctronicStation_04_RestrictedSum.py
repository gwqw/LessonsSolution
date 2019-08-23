def checkio(data):
    if len(data) > 0:
        return data[0] + checkio(data[1:])
    else:
        return 0


print(checkio([1, 2, 3, 4, 5]))
