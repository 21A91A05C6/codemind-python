def reverse_vowels(s):
	vowels = ""
	for i in s:
		if i in "aeiouAEIOU":
			vowels += i
	result_string = ""
	for i in s:
		if i in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += i
	return result_string
s=input()
print(reverse_vowels(s))