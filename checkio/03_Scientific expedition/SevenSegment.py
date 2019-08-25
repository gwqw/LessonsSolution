"""
    7-segment Display displays 2 digits. Some segments are not working
     A   numeration of segments
    F B
     G
    E C
     D

    Input: [{set of lit segmets}, {set of broken segments}]
    Output: Total number that device can display

    Algo:
    split: lit1, lit2, broken1, broken2
    for every symbol (s): NUM /\ lit = lit, NUM /\ (lit U broken) = NUM: s1 += s
    count total numbers from s1 n s2
"""

DIGITS = {1:{'B', 'C'}, 2:{'A', 'B', 'G', 'E', 'D'}, 3:{'A', 'B', 'G', 'C', 'D'},
          4:{'F', 'G', 'B', 'C'}, 5:{'A', 'F', 'G', 'C', 'D'},
          6:{'A', 'F', 'G', 'C', 'D', 'E'}, 7:{'A', 'B', 'C'},
          8:{'A', 'B', 'F', 'G', 'C', 'D', 'E'}, 9:{'A', 'B', 'F', 'G', 'C', 'D'},
          0:{'A', 'B', 'F', 'C', 'D', 'E'}
         }

def split(seg):
    lit1 = set()
    lit2 = set()
    for c in seg:
        if c >= 'A' and c <= 'G':
            lit1.add(c.upper())
        else:
            lit2.add(c.upper())
    return lit1, lit2

def seven_segment(lit_seg, broken_seg):
    # split
    lit1, lit2 = split(lit_seg)
    broken1, broken2 = split(broken_seg)
    # find symbols
    s1 = []
    s2 = []
    for i in range(10):
        d = DIGITS[i]
        if (d & lit1) == lit1 and (d & (lit1 | broken1)) == d:
            s1.append(i)
        if (d & lit2) == lit2 and (d & (lit2 | broken2)) == d:
            s2.append(i)
    # count total
    return len(s1) * len(s2)


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
