match = 1
mismatch = -1
gap = -3

def align(a1, a2):
    matrix = [[0 for _ in range(len(a1) + 1)] for _ in range(len(a2) + 1)]
    for i in range(1, len(a1) + 1):
        matrix[0][i] = matrix[0][i-1] + 0
    for i in range(1, len(a2) + 1):
        matrix[i][0] = matrix[i-1][0] + 0
    for i in range(1, len(a1)+1):
        for j in range(1, len(a2)+1):
            a_i, a_j = a1[i-1], a2[j-1]
            if a_i == a_j:
                diag = match
            else:
                diag = mismatch
            matrix[j][i] = max([matrix[j-1][i] + gap, matrix[j][i-1] + gap, matrix[j-1][i-1] + diag, 0])
    print(matrix)

align('GGTTTAAGCCGT', 'ACGT')

"""
[[ 0, -4,  -8,-12,-16,-20,-24,-28],
 [-4, -3,  -7, -3, -7,-11,-15,-19],
 [-8, -7,   2, -2, -6, -2, -6,-10],
 [-12,-11, -2,  7,  3, -1, -5, -9],
 [-16,-15, -6,  3,  4,  8,  4,  0],  
 [-20,-19,-10, -1,  0,  4, 13,  9],
 [-24,-15,-14, -5, -4,  0,  9, 10]]
"""