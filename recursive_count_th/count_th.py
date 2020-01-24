'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
arr = []
def count_th(word):
	# BASE CASE
	if len(word) <= 1:
		return len(arr)

	if word[0] + word[1] == 'th':
		new_word = word[0] + word[1]
		arr.append(new_word)

	return count_th(word[1:]) 
    