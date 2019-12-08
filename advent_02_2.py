# advent of code day 2

def int_converter(x):
	return int(x)


def get_file(filename):
	with open(filename, 'r') as f:
		for line in f.readlines():
			intcode = list(map(int_converter, line.split(',')))
			return intcode


def int_solver(intcode, x, y):
	intcode[1] = x
	intcode[2] = y

	for n in range(0, len(intcode), 4):
		if intcode[n] == 99:
			return intcode[0]

		first_pos = intcode[intcode[n + 1]]
		second_pos = intcode[intcode[n + 2]]

		if intcode[n] == 1:
			intcode[intcode[n + 3]] = first_pos + second_pos

		elif intcode[n] == 2:
			intcode[intcode[n + 3]] = first_pos * second_pos


for x in range(0, 100):
	for y in range(0, 100):
		code = get_file('intcode_02.txt')
		answer = int_solver(code, x, y)
		if answer == 19690720:
			print(x, y)