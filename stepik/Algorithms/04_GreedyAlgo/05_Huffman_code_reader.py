"""
    Input
    1 1  <- different letters, code size
    a: 0 <- code table
    0    <- code to decrypt
"""

if __name__ == "__main__":
    # input parser
    k, l = input().split()
    k, l = int(k), int(l)
    decode_table = {}
    for i in range(k):
        w = input().split(':')
        decode_table[w[1].strip()] = w[0]
    code = input()
    #print(decode_table)
    res_str = ""
    cc = ""
    for c in code:
        cc += c
        if cc in decode_table:
            res_str += decode_table[cc]
            cc = ""
    print(res_str)
