import numpy as np
import random
import math

def distancePhylo(m):
    all = {i for i in range(m.shape[0])}
    m[m == 0] = 100
    index = np.where(m == np.amin(m))
    x, y = index[0][0], index[0][1]
    m[m == 100] = 0
    a = list(all - {x, y})
    a.sort()
    next = np.empty((m.shape[0]-1, m.shape[0]-1)).astype(float)
    for i in range(m.shape[0] - 2):
        for j in range(m.shape[0] - 2):
            next[i][j] = m[a[i]][a[j]]
        next[i][j + 1] = (m[a[i]][x] + m[a[i]][y] - m[x][y])/2
        next[j + 1][i] = (m[a[i]][x] + m[a[i]][y] - m[x][y])/2
    next = np.around(next, 3)
    print(next)
    return next

def neighbourJoining(m):
    s = np.reshape(np.sum(m, axis = 0), (-1, m.shape[0]))
    i_inv = 1 - np.eye(m.shape[0])
    s = (s + s.T) * i_inv
    m_ = (m * (m.shape[0] - 2) - s).astype(int)
    all = {i for i in range(m.shape[0])}
    m_[m_ == 0] = 100
    index = np.where(m_ == np.amin(m_))
    x, y = index[0][0], index[0][1]
    m_[m_ == 100] = 0
    a = list(all - {x, y})
    a.sort()
    next = np.empty((m.shape[0] - 1, m.shape[0] - 1)).astype(float)
    for i in range(m.shape[0] - 2):
        for j in range(m.shape[0] - 2):
            next[i][j] = m[a[i]][a[j]]
        next[i][j + 1] = (m[a[i]][x] + m[a[i]][y] - m[x][y]) / 2
        next[j + 1][i] = (m[a[i]][x] + m[a[i]][y] - m[x][y]) / 2
    next = np.around(next, 3)
    print(next)
    return m


# m = [[0, 3, 6, 4],
#      [3, 0, 7, 5],
#      [6, 7, 0, 2],
#      [4, 5, 2, 0]]

m = [[0, 13, 21, 22],
     [13, 0, 12, 13],
     [21, 12, 0, 13],
     [22, 13, 13, 0]]

m = neighbourJoining(np.array(m))