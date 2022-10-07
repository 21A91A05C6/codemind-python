from itertools import permutations
def allPermutations(str):
	per = permutations(str)
	k=""
	for i in list(per):
		print("".join(i))
s =input()
allPermutations(s)
