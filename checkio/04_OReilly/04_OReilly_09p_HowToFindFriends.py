def addToSet(element, network, conset):
    conset.add(element)
    for c in network:
        if element == c[0] and c[1] not in conset:
            addToSet(c[1], network, conset)
        elif element == c[1] and c[0] not in conset:
            addToSet(c[0], network, conset)           

def check_connection(network, first, second):
    print(f"fisrt = {first}, second = {second}")
    # form list network
    network = [c.split('-') for c in network]
    # form first network
    fset = set()
    addToSet(first, network, fset)
    print(fset)
    # check second
    return second in fset

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
