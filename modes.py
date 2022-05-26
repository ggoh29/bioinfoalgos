# plain = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
plain = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cipher = ['D', 'G', 'W', 'X', 'T', 'E', 'R', 'L', 'Y', 'Z', 'O', 'J', 'N',
          'S', 'I', 'Q', 'P', 'C', 'U', 'H', 'B', 'V', 'F', 'A', 'M', 'K']
encoding = [i for i in range(len(plain))]


def f(x, y):
    return (x + y) % 26

def f_(x, y):
    return (x - y) % 26


def ecb(code):
    p = [plain[cipher.index(letter)] for letter in code]
    return p


def cbc(code):
    p = []
    for iv, x in zip(code[:-1], code[1:]):
        iv_ = encoding[plain.index(iv)]
        x_ = encoding[cipher.index(x)]
        p.append(plain[f_(x_, iv_)])
    return p


def cfb(code):
    p = []
    for iv, x in zip(code[:-1], code[1:]):
        iv_ = cipher[plain.index(iv)]
        iv_ = encoding[plain.index(iv_)]
        x_ = encoding[plain.index(x)]
        p.append(plain[f_(x_, iv_)])
    return p


def ofb(code):
    iv = encoding[plain.index(code[0])]
    p = []
    for c in code[1:]:
        iv = encoding[plain.index(cipher[iv])]
        c_ = encoding[plain.index(c)]
        p.append(plain[f_(c_, iv)])
    return p


print(ecb(list('UOMHDJT')))
print(cfb(list('RVPHTUH')))
print(ofb(list('LNMSUUY')))
