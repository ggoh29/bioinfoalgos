import numpy as np

def create_dct(input):
    dct = {}
    for i in range(len(input)):
        if input[i] in dct:
            dct[input[i]].append(i)
        else:
            dct[input[i]] = [i]
    return dct


def bwt(input):
    original = []
    s = sorted(a)
    dct_start = create_dct(input)
    dct_end = create_dct(s)
    start = 0
    while len(original) != len(input):
        start_char = s[start]
        count = 0
        for i in range(start):
            if s[i] == start_char:
                count += 1
        last_char = s[dct_end[start_char][count]]
        original.append(last_char)
        start = dct_start[last_char][count]
    print(original)

a = 'atttaa$g'
a = list(a)
# a = ['e', 'n', 'w', 'v', 'p', 'e', 'o', 's', 'e', 'u', '$', 'l', 'l', 't']
bwt(a)