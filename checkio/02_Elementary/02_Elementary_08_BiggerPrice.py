def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    res = []
    while len(res) < limit:
        max_price = 0
        max_d = {}
        for d in data:
            if d["price"] > max_price and not d in res:
                max_price = d["price"]
                max_d = {}
                max_d["name"] = d["name"]
                max_d["price"] = d["price"]
        res.append(max_d)                
    return res


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
