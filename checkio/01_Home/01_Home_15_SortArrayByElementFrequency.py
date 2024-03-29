"""
    input: itterable
    output: sorted descending: first elements with most frequency in input/
    if freq are equal: as first appearance
"""

def frequency_sort(items):
    n = len(items)
    from collections import Counter
    counter = Counter(items)
    order = dict()
    for i, item in enumerate(items):
        if item not in order:
            order[item] = i
    return sorted(items, key=lambda x: counter[x] + 1 - order[x] / n, reverse=True)
    


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
