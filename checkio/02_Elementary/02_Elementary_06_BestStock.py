def best_stock(data):
    max_rate = 0.0
    stock_name = ''
    for k,v in data.items():
        if v > max_rate:
            max_rate = v
            stock_name = k
    return stock_name


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
