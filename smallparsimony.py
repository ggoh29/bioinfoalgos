import math

DNA = ['A', 'C', 'G', 'T']
I = [[0, 1, 1, 1],
		 [1, 0, 1, 1],
		 [1, 1, 0, 1],
		 [1, 1, 1, 0]]

def smallparsimony(tree):
	c = []
	for t in tree:
		c.append([[math.inf, math.inf, math.inf, math.inf] for _ in range(len(t))])
	for i in range(len(tree) - 1, -1, -1):
		for j in range(len(tree[i])):
			if tree[i][j] in DNA:
				c[i][j][DNA.index(tree[i][j])] = 0
			else:
				for k in range(4):
					I_k = I[k]
					daughter = [a + b for a,b in zip(I_k, c[i + 1][2 * j])]
					son = [a + b for a,b in zip(I_k, c[i + 1][2 * j + 1])]
					c[i][j][k] = min(daughter) + min(son)
	for thing in c:
		print(thing)
	print("")
	tree[0][0] = DNA[c[0][0].index(min(c[0][0]))]
	for i in range(0, len(tree) - 1):
		for j in range(len(c[i])):
			k = DNA.index(tree[i][j])
			I_k = I[k]
			daughter = [a + b for a, b in zip(I_k, c[i + 1][2 * j])]
			son = [a + b for a, b in zip(I_k, c[i + 1][2 * j + 1])]
			i_d, i_s = DNA[daughter.index(min(daughter))], DNA[son.index(min(son))]
			tree[i + 1][2 * j], tree[i+1][2 * j + 1] = i_d, i_s
	for thing in tree:
		print(thing)





tree = [[0],
				[0, 0],
				[0, 0, 0, 0],
				['C', 'C', 'A', 'C', 'G', 'G', 'T', 'C']]
smallparsimony(tree)