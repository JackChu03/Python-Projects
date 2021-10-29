"""
File: boggle.py
Name: Jack
----------------------------------------
We want to create a boggle game, so that if we input a 4*4 board, we can get every word in that board
(every neighbor of a word could work to form a word, the word could be found in a dictionary)
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TO Create a 4*4 boggle game
	"""
	####################
	# 'board' collects every character we input
	board = []
	# 'all words list' is a list that contains all words found in the board
	all_words_list = []
	# n just controls when to go out of the loop
	n = 1
	# the loop is for the starting input
	while n <= 4:
		row = input(f'{n} rows or letters: ')
		row = row.lower()
		row_list = row.split()
		if len(row_list) != 4:
			print('illegal format')
			n = 6
		if n != 6:
			for ch in row_list:
				if len(ch) != 1:
					print('illegal format')
					n = 6
		board.append(row_list)
		n = n+1
	start = time.time()
	# if not illegal format, then start to find!
	if n == 5:
		# to get each word in the board
		for y in range(len(board)):
			for x in range(len(board[y])):
				ch = board[y][x]
				point = [y, x]
				# 'touch point list' is a list that contains the characters we've already chosen
				touch_point_lst = [point]
				single_ch_words = recursion(ch, board, '', [], touch_point_lst, y, x, 4, all_words_list)
				# to loop over every words found in every character
				for word in single_ch_words:
					if word not in all_words_list:
						all_words_list.append(word)
		print(f'There are {len(all_words_list)} words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def recursion(ch, board, cur_word, all_find_word_lst, touch_point_list, y, x, k, all_words_list):
	"""
	:param ch: (str) the character we choose from the board
	:param board: (list) stands for the 4*4 board
	:param cur_word: (str) the string waiting to be loop over
	:param all_find_word_lst: (list) contains the words we've already found in this character
	:param touch_point_list: (list) a list that contains the characters we've already chosen
	:param y: (int) the y coordinate of the character in the board
	:param x: (int) the x coordinate of the character in the board
	:param k: (int) controls the bottom limit of how many words should form a word
	:param all_words_list: (list) contains the words we've already found in all previous characters
	:return: (list) all_find_word_list
	"""
	dic = read_dictionary()
	if cur_word in dic and len(cur_word) >= k:
		# double check if we already got the word
		if cur_word not in all_find_word_lst and cur_word not in all_words_list:
			all_find_word_lst.append(cur_word)
			print(f'Found: "{cur_word}"')
			# still go recursion even if we've already found a word in dictionary (keep checking if there's other words)
			# choose '16' because it's a 4*4 board game, the longest word can not exceed 16 characters
			if len(cur_word) <= 16:
				recursion(ch, board, cur_word, all_find_word_lst, touch_point_list, y, x, k+1, all_words_list)
	else:
		if cur_word == '':
			cur_word = cur_word + ch
		# to find the neighbors of the character
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= y+i < len(board):
					if 0 <= x+j < len(board[y]):
						if [y+i, x+j] not in touch_point_list:
							neighbor_ch = board[y+i][x+j]
							touch_point_list.append([y+i, x+j])
							cur_word = cur_word + neighbor_ch
							# to check if the start of the current word so far exists in the dictionary or not
							if has_prefix(cur_word):
								recursion(neighbor_ch, board, cur_word, all_find_word_lst, touch_point_list, y+i, x+j, k, all_words_list)
								# backtracking
								cur_word = cur_word[:len(cur_word) - 1]
								touch_point_list.pop()
							else:
								# backtracking
								cur_word = cur_word[:len(cur_word) - 1]
								touch_point_list.pop()
	return all_find_word_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# To get a list of the dictionary
	python_list = []
	with open(FILE, 'r') as f:
		for line in f:
			line_l = line.split()
			python_list.append(line_l[0])
	return python_list


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	lst = read_dictionary()
	for word in lst:
		if word.startswith(sub_s):
			return True
		else:
			pass
	return False


if __name__ == '__main__':
	main()
