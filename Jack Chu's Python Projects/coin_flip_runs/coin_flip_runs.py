"""
File: coin_flip_runs.py
Name: Jack Chu
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	To execute the flip, we need 4 variables(ans, n, rn, x),
	First, to select H or T randomly
	Then, to get the number of row by the input
	In the end, decide when to stop the random
	"""
	ans = ''
	n = -1
	# n stands for the later which number in the letter of ans
	rn = 0
	# rn stands for how many rows we get so far
	print("Let's flip a coin!")
	x = int(input('Numbers of Runs: '))
	# to get the number of row
	while True:
		# first, get random H or T
		if r.random() > 0.5:
			ans = ans + 'H'
		else:
			ans = ans + 'T'
		n = n + 1
		# each time, get one more letter
		if n >= 2:
			# first special occasion
			if ans[n-1] == ans[n-2] and ans[n-1] != ans[n]:
				rn = rn + 1
		elif n == 1 and x == 1:
			# second special occasion
			if ans[n] == ans[n-1]:
				rn = rn + 1
		else:
			# third special occasion
			pass
		if rn == x:
			# if rn is same with the row we want, stop
			break
	if n >= 2:
		# determine when to cut the string
		ans = ans[0:n]
		while ans[n-1] == ans[n-3]:
			# special occasion: when too many same letter in last row
			n = n-1
			ans = ans[0:n]
	print(ans)




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
