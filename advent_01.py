# advent of code day 1
import math

def fuel(modules):
	new = []
	for n in modules:
		n = int(n)
		adjusted = ((n // 3) - 2)
		new.append(adjusted)
	print(sum(new))


def get_list(file_name):
	with open(file_name, 'r') as f:
		modules = []
		for line in f:
			modules.append(int(line))
	return modules		


def new_fuel(modules):
	new = []
	for num in modules:
		temp = math.floor((num // 3) - 2)
		new.append(temp)

		while temp > 0:
			temp = math.floor((temp // 3) - 2)

			if temp > 0:
				new.append(temp)

	return sum(new)


modules = get_list('modules.txt')
fuel(modules)

answer = new_fuel(modules)
print(answer)
