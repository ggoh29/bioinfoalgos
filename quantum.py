import math
import numpy as np

X = np.array([[0, 1.], [1., 0]])
H = np.array([[1, 1], [1, -1]])/math.sqrt(2)
I = np.array([[1., 0], [0, 1.]])
T = np.array([[1, 0], [0, (1 + 1j)/math.sqrt(2)]])
S = T @ T
CNOT = np.array([[1., 0, 0, 0],
                 [0, 1., 0, 0],
                 [0, 0, 0, 1.],
                 [0, 0, 1., 0]])
SWAP = np.array([[1., 0, 0, 0],
                 [0, 0, 1., 0],
                 [0, 1., 0, 0],
                 [0, 0, 0, 1.]])
SWAP2 = np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 1., 0., 0., 0.],
                  [0., 0., 1., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 1., 0.],
                  [0., 1., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 1., 0., 0.],
                  [0., 0., 0., 1., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 1.]])

CNOT2 = np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                  [0., 1., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 1., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 1., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 1., 0., 0.],
                  [0., 0., 0., 0., 1., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 1.],
                  [0., 0., 0., 0., 0., 0., 1., 0.]])

R2 = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0 - 1j]])

S2 = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0 + 1j]])

q = math.sqrt(2)
R3t = np.array([[q, 0., 0., 0., 0., 0., 0., 0.],
                [0., q, 0., 0., 0., 0., 0., 0.],
                [0., 0., q, 0., 0., 0., 0., 0.],
                [0., 0., 0., q, 0., 0., 0., 0.],
                [0., 0., 0., 0., q, 0., 0., 0.],
                [0., 0., 0., 0., 0., 1-1j, 0., 0.],
                [0., 0., 0., 0., 0., 0., q, 0.],
                [0., 0., 0., 0., 0., 0., 0., 1-1j]])/q

T3t = np.array([[q, 0., 0., 0., 0., 0., 0., 0.],
                [0., q, 0., 0., 0., 0., 0., 0.],
                [0., 0., q, 0., 0., 0., 0., 0.],
                [0., 0., 0., q, 0., 0., 0., 0.],
                [0., 0., 0., 0., q, 0., 0., 0.],
                [0., 0., 0., 0., 0., 1+1j, 0., 0.],
                [0., 0., 0., 0., 0., 0., q, 0.],
                [0., 0., 0., 0., 0., 0., 0., 1+1j]])/q

ZERO = np.array([[1.], [0.]])
ONE = np.array([[0.], [1.]])
Bp = np.array([[1/q], [1/q]])
Bm = np.array([[1/q], [-1/q]])

# bigU1 = np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
#                   [0., 1., 0., 0., 0., 0., 0., 0.],
#                   [0., 0., 0., 0 - 1j, 0., 0., 0., 0.],
#                   [0., 0., 0 + 1j, 0., 0., 0., 0., 0.],
#                   [0., 0., 0., 0., 1., 0., 0., 0.],
#                   [0., 0., 0., 0., 0., 1., 0., 0.],
#                   [0., 0., 0., 0., 0., 0., 0., 0 - 1j],
#                   [0., 0., 0., 0., 0., 0., 0 + 1j, 0.]])
#
# bigU2 = np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
#                   [0., 1., 0., 0., 0., 0., 0., 0.],
#                   [0., 0., 1., 0., 0., 0., 0., 0.],
#                   [0., 0., 0., 1., 0., 0., 0., 0.],
#                   [0., 0., 0., 0., 0., 0 - 1j, 0., 0.],
#                   [0., 0., 0., 0., 0 + 1j, 0., 0., 0.],
#                   [0., 0., 0., 0., 0., 0., 0., 0 - 1j],
#                   [0., 0., 0., 0., 0., 0., 0 + 1j, 0.]])

def inverse_u(U):
    u = np.identity(4)
    for i in range(2):
        for j in range(2):
            u[((i +1)*2)-1][((j +1)*2)-1] = U[i][j]
    return u

def controlled_u(U, size = 2):
    u = np.identity(2**size)
    x, y = u.shape
    x, y = x//2, y//2
    for i in range(size - 1):
        u[x:x+U.shape[0], y:y+U.shape[1]] = U
        x += U.shape[0]
        y += U.shape[1]
    return u

def tp(x , y):
    x_size = x.shape
    y_size = y.shape
    t = [[0 for _ in range(x_size[1] * y_size[1])] for _ in range(x_size[0] * y_size[0])]
    for x_i in range(x_size[0]):
        for x_j in range(x_size[1]):
            for y_i in range(y_size[0]):
                for y_j in range(y_size[1]):
                    t[y_i + x_i * y_size[0]][y_j + x_j * y_size[1]] = x[x_i][x_j] * y[y_i][y_j]
    return np.array(t)

def QPE(m, u, size=3):
    psi1 = I
    for _ in range(size - 1):
        psi1 = tp(H, psi1)
    m = psi1 @ m
    for s in range(2, size+1):
        psi = controlled_u(u, size=s)
        for _ in range(size - s):
            psi = tp(I, psi)
        for _ in range(2 ** (s - 2)):
            m = np.round(psi @ m, 4)

    return np.round(m, 4)

def QFT(m, size = 3):
    if size == 4:
        psi1 = tp(tp(tp(H, I), I), I)
        psi2 = tp(tp(S2, I), I)
        psi3 = tp(T3t, I)
        psi4 = tp(tp(tp(I, H), I), I)
        psi5 = tp(I, tp(S2, I))
        psi6 = tp(tp(tp(I, I), H), I)
        m = psi6 @ psi5 @ psi4 @ psi3 @ psi2 @ psi1 @ m

    elif size == 3:
        psi2 = tp(tp(H, I), I)
        psi3 = tp(S2, I)
        psi4 = tp(tp(I, H), I)
        m = psi4 @ psi3 @ psi2 @ m

    s = SWAP if size == 3 else SWAP2
    m = tp(s, I) @ m

    return np.round(m, 4)

def inverse_QFT(m, size = 3):
    s = SWAP if size == 3 else SWAP2
    m = tp(s, I) @ m

    if size == 4:
        psi2 = tp(tp(tp(I, I), H), I)
        psi3 = tp(I, tp(R2, I))
        psi4 = tp(tp(tp(I, H), I), I)
        psi5 = tp(R3t, I)
        psi6 = tp(tp(R2, I), I)
        psi7 = tp(tp(tp(H, I), I), I)
        x = psi7 @ psi6 @ psi5 @ psi4 @ psi3 @ psi2 @ m

    elif size == 3:
        psi2 = tp(tp(I, H), I)
        psi3 = tp(R2, I)
        psi4 = tp(tp(H, I), I)
        x = psi4 @ psi3 @ psi2 @ m

    return np.round(x, 4)

i = np.array([[0.], [-1.]])/math.sqrt(2)
j = np.array([[1], [0 + 1j]])/math.sqrt(2)
k = np.array([[math.sqrt(2)], [1 + 1j]])/math.sqrt(2)
e1 = np.array([[0 + 1j], [1]])/math.sqrt(2)
e2 = np.array([[0 - 1j], [1]])/math.sqrt(2)

m = tp(tp(tp(ZERO, ZERO), ZERO), e1)
# u = np.array([[1, 2], [2, -1]])/math.sqrt(5)
u = np.array([[1, -1], [1, 1]])/math.sqrt(2)
# u = np.array([[0, 0-1j], [0+1j, 0]])
qpe = QPE(m, u, size = 4)
print(inverse_QFT(qpe, size=4))
# # qpe should be the same as (|00>|0> + |01>u|0> + |10>u^2|0> + |11>u^3|0>)/2
# one = tp(tp(ZERO, ZERO), ZERO)
# two = tp(tp(ZERO, ONE), u @ ZERO)
# thr = tp(tp(ONE, ZERO), u @ u @  ZERO)
# fou = tp(tp(ONE, ONE), u @ u @ u @ ZERO)
# assert((qpe == np.around((one + two + thr + fou)/2, 4)).all())

one = tp(tp(tp(ZERO, ZERO), ZERO), ZERO)
two = tp(tp(tp(ZERO, ZERO), ONE),u @ ZERO)
thr = tp(tp(tp(ZERO, ONE), ZERO),u @ u @ ZERO)
fou = tp(tp(tp(ZERO, ONE), ONE), u @ u @ u @ ZERO)
fiv = tp(tp(tp(ONE, ZERO), ZERO),u @ u @ u @ u @ ZERO)
six = tp(tp(tp(ONE, ZERO), ONE), u @ u @ u @ u @ u @ ZERO)
sev = tp(tp(tp(ONE, ONE), ZERO), u @ u @ u @ u @ u @ u @ ZERO)
eig = tp(tp(tp(ONE, ONE), ONE),  u @ u @ u @ u @ u @ u @ u @ ZERO)

# print(tp(tp(tp(i, j), k), (-e1 + e2)))
# print(inverse_QFT(tp(tp(tp(i, j), k), (-e1 + e2)), size=4))
# print(QFT(inverse_QFT(tp(tp(tp(i, j), k), (-e1 + e2)), size=4), size=4))
# print(tp(tp(tp(i, j), k), (-e1 + e2)))
#
# # print(qpe)
# m = tp(tp(tp(ZERO, ZERO), ZERO), e1)

