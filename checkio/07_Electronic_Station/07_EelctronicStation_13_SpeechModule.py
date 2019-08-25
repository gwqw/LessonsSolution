"""
    Write number with words:
    4 -> four
    0 < number < 1000
"""

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    # find ones, tens, hundreds
    ones = number % 10
    tens = (number - ones) // 10 % 10
    hundreds = (number - tens*10 - ones) // 100
    # write number
    need_space = False
    res = ""
    if hundreds:
        res = FIRST_TEN[hundreds-1] + " " + HUNDRED
        need_space = True
    if tens == 1:
        if need_space: res += " "
        res += SECOND_TEN[ones]
        return res
    
    if tens >= 2:
        if need_space: res += " "
        res += OTHER_TENS[tens-2]
        need_space = True
    if ones:
        if need_space: res += " "
        res += FIRST_TEN[ones-1]
    
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
