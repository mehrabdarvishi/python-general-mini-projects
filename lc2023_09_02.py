dictionary = ['s', 'say', 'hello', 'wo', 'world', 'for', 'worl', 'geeks', 'sayh', 'me', 'turn']
s = 'sayhelloworld'
substrings = []
for word in dictionary:
	word_start_index = s.find(word)
	word_end_index = word_start_index + len(word) - 1
	is_optimal_substring = True
	# If selected word from dictionary was found in the string.
	if word_start_index != -1:
		for substring_index, substring in enumerate(substrings):
			# If a substring had the selected word in it, That means we have a longer word in the dictionary and just don't consider the shorter one. (It is not optimal)
			if substring.find(word) != -1:
				is_optimal_substring = False
				break
			substrings_start_index = s.find(substring)
			substrings_end_index = substrings_start_index + len(substring) - 1
			not_overlapping = not((substrings_start_index <= word_end_index <= substrings_end_index) or (substrings_start_index <= word_start_index <= substrings_end_index))
			print('*'*50)
			print(word, word_start_index, word_end_index)
			print(substring, substrings_start_index, substrings_end_index)
			print('word.find(substring)', word.find(substring))
			print(not_overlapping)
			print('*'*50)
			if not not_overlapping:
				substrings.pop(substring_index)
			# if better (longer) substring was found, remove the short one.		
			if word.find(substring) != -1 and not_overlapping:
				print('rewfwaf')
				substrings.pop(substring_index)
		if is_optimal_substring:
			substrings.append(word)
print(substrings)