import math


def entropy(x):
    x = [1 if i == 0 else i for i in x]
    x = [-i * math.log2(i) for i in x]
    return sum(x)


def kl_divergence(x, y):
    x, y = [1 if i == 0 else i for i in x], [1 if i == 0 else i for i in y]
    kl = [i * math.log2(i / j) for i, j in zip(x, y)]
    return sum(kl)


def cross_entropy(x, y):
    return kl_divergence(x, y) + entropy(x)


def joint_entropy(matrix):
    matrix = [[1 if i == 0 else i for i in x] for x in matrix]
    return sum([sum([- i * math.log2(i) for i in x]) for x in matrix])


def mutual_info(matrix):
    x, y = [sum(i) for i in zip(*matrix)], [sum(i) for i in matrix]
    return entropy(x) + entropy(y) - joint_entropy(matrix)


print(entropy([1 / 8, 1 / 8, 1 / 4, 1 / 2]))
# print(kl_divergence([1 / 8, 1 / 8, 1 / 4, 1 / 2], [1 / 4, 1 / 4, 1 / 4, 1 / 4]))
# print(cross_entropy([1 / 8, 1 / 8, 1 / 4, 1 / 2], [1 / 4, 1 / 4, 1 / 4, 1 / 4]))
# print(joint_entropy([[1 / 8, 1 / 16, 1 / 32, 1 / 32],
#                      [1 / 16, 1 / 8, 1 / 32, 1 / 32],
#                      [1 / 16, 1 / 16, 1 / 16, 1 / 16],
#                      [1 / 4, 0, 0, 0]]))
# print(mutual_info([[1 / 8, 1 / 16, 1 / 32, 1 / 32],
#                    [1 / 16, 1 / 8, 1 / 32, 1 / 32],
#                    [1 / 16, 1 / 16, 1 / 16, 1 / 16],
#                    [1 / 4, 0, 0, 0]]))
