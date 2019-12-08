# advent of code day 2

def int_converter(x):
	return int(x)


def get_file(filename):
	with open(filename, 'r') as f:
		for line in f.readlines():
			intcode = list(map(int_converter, line.split(',')))
			return intcode


def int_solver(intcode):
	intcode[1] = 12
	intcode[2] = 2

	for n in range(0, len(intcode), 4):
		if intcode[n] == 99:
			return intcode[0]

		first_pos = intcode[intcode[n + 1]]
		second_pos = intcode[intcode[n + 2]]

		if intcode[n] == 1:
			intcode[intcode[n + 3]] = first_pos + second_pos

		elif intcode[n] == 2:
			intcode[intcode[n + 3]] = first_pos * second_pos


code = get_file('intcode_02.txt')

print(int_solver(code))