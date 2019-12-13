# advent of code day 3

#######################
# THIS IS STOLEN
#######################

# dict where key is a touple of x and y elements
# the value is 0 if not set, and 1 if it is set
# make a list of all line; the beginning and end
# then sort them by distance to the original point
# and some more stuff....


A,B,_ = open('day3.txt').read().split('\n')
# A is the first part of the text file, and we are splitting it by the line
# tuple with 3 elements... need under score because there are too many elements to unpack

A,B = [x.split(',') for x in [A,B]]
# Every item in the list is separated by a comma,  and the 2 lines A and B are two separate elements
# A and B are the two lines in the text file

delta_X = {
	'L': -1,
	'R': 1,
	'U': 0,
	'D': 0
}
# describing the change in the X direction

delta_Y = {
	'L': 0,
	'R': 0,
	'U': 1,
	'D': -1
}
# describing the change in the Y direction

def get_points(A):
	x = 0
	y = 0
	length = 0
	# initializing some begining values

	ans = {}
	# right now, an empty dictionary

	for find in A:
		# this is a for loop
		d = find[0]
		# variable d is equal to an item in list A at position 0
		n = int(find[1:])
		# variable n is equal to integer in 'find', from pos 1 to the end

		assert d in ['L', 'R', 'U', 'D']
		# assert means if something is TRUE, do nothing.  if false, tell me

		for _ in range(n):
			# for 'idc' in the range of numbers in variable n...
			
			x += delta_X[d]
			y += delta_Y[d]
			# for above... variables x and y are now set to the position 'd' in the previous
			# dictionaries that I set up

			length += 1
			# after every action in the for loop, length is increasing by 1

			if (x, y) not in ans:
				ans[(x, y)] = length
				# if loop...  if variables x and y are not in the ans dict...
				# dict key with values x and y is equal to variable length

	return ans
	# function is returning the dictionary

partA = get_points(A)
partB = get_points(B)
# running the above functions, with the parameters being the lists of numbers for the 2 wires

both = set(partA.keys())&set(partB.keys())
# using the dictionary keys

part1 = min([abs(x) + abs(y) for (x, y) in both])
# returns the smallest element in a list; the absolute values of x and y positions

part2 = min([partA[p]+partB[p] for p in both])
# getting a value from the dictionaries if the value 'p' is in both

print(part1, part2)
# answers





