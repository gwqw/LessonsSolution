import datetime

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date1 = datetime.date(*date1)
    date2 = datetime.date(*date2)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
