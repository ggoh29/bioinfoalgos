comp_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def nussinov(s):
	matrix = [[0 for _ in range(len(s))] for _ in range(len(s))]
	for i in range(len(s)):
		for j in range(i + 1, len(s)):
			y, x = j, j - i - 1
			c = int(comp_pairs[s[x]] == s[y])
			m = max([matrix[x][k] + matrix[k + 1][y] for k in range(x, y)])
			matrix[x][y] = max([matrix[x + 1][y], matrix[x][y - 1], matrix[x + 1][y - 1] + c, m])
	for t in matrix:
		print(t)


example = 'GGGAAATCC'
example = list(example)
nussinov(example)
