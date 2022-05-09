states = ['S', 'H', 'L']
symbols = ['A', 'C', 'G', 'T']
emission = [[0, 0, 0, 0], [0.2, 0.3, 0.3, 0.2], [0.3, 0.2, 0.2, 0.3]]
transition = [[0, 0.5, 0.5], [0, 0.5, 0.5], [0, 0.4, 0.6]]

def viterbi(sequence):
	matrix = [[0 for _ in range(len(states))] for _ in range(len(sequence) + 1)]
	matrix[0][0] = 1
	for i in range(1, len(sequence) + 1):
		for j in range(len(states)):
			e = symbols.index(sequence[i - 1])
			transition_probs = [transition[k][j] for k in range(len(states))]
			matrix[i][j] = emission[j][e] * max([a * b for a, b in zip(transition_probs, matrix[i - 1])])

	print(matrix)
	output = []
	for thing in matrix:
		output.append(states[thing.index(max(thing))])
	print(output)

def forward(sequence):
	matrix = [[0 for _ in range(len(states))] for _ in range(len(sequence) + 1)]
	matrix[0][0] = 1
	for i in range(1, len(sequence) + 1):
		for j in range(len(states)):
			e = symbols.index(sequence[i - 1])
			transition_probs = [transition[k][j] for k in range(len(states))]
			matrix[i][j] = emission[j][e] * sum([a * b for a, b in zip(transition_probs, matrix[i - 1])])

	print(matrix)
	output = []
	for thing in matrix:
		output.append(states[thing.index(max(thing))])
	print(output)

emit = 'GGCACTGAA'
forward(emit)