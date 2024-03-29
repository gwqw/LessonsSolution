def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    # format base
    power_index = 0
    base_num = base
    while abs(number) >= base_num and power_index < len(powers)-1:
        base_num *= base
        power_index += 1
    number /= base**power_index
    #print(number)
        
    #decimals
    format_string = ""
    if decimals != 0:
        format_string = "%." + str(decimals) + "f"
    else:
        format_string = "%d"
    res = format_string % (number)
    res += powers[power_index] + suffix

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
    assert friendly_number(-150, base=100, powers=["","d","D"]) == "-1d", '-1d'
    assert friendly_number(255000000000, powers=["","k","M"]) == '255000M', '255000M'
    assert friendly_number(10**24) == '1Y', '1Y'
    assert friendly_number(10**32) == '100000000Y', '100000000Y'
