"""
Name: Jack
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global
python_list = []


def main():
    """
    TODO: To get all the anagrams of the input word in the console from the dictionary
    """
    ####################
    print('Welcome to "Anagram Generator!" (or press -1 to leave)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        start = time.time()
        print('Searching...')
        n, anagrams_list = find_anagrams(s)
        print(n, 'anagrams:', anagrams_list)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
    ####################


def read_dictionary():
    # To get a list of the dictionary
    with open(FILE, 'r') as f:
        for line in f:
            line_l = line.split()
            python_list.append(line_l[0])
    return python_list


def find_anagrams(s):
    """
    to find all anagrams of the input word, but need a helper function to do so
    """
    n, anagrams_list = helper_find_anagrams(s, 0, [])
    return n, anagrams_list


def helper_find_anagrams(s, n, anagrams_list):
    """
    :param s: stands for the input word
    :param n: n is a counter for the number of anagrams
    :param anagrams_list: to collect all anagrams we want
    :return: n, anagrams_list
    """
    # first to get the list of each characters of the input word 's'
    s_list = list_manipulation(s)
    # To get the all permutation characters of the input word
    all_nums = all_nums_list(s_list, '', [])
    # To get all words, we need to again transform the list of all numbers permutations to words list
    all_words = change_all_nums(all_nums, s_list)
    py_list = read_dictionary()
    # to decide if the words in the dictionary list, if in, then it's the word we want
    for word in all_words:
        if word in py_list:
            anagrams_list.append(word)
            n = n + 1
            print('Found:', anagrams_list[len(anagrams_list) - 1])
            print('Searching...')
    return n, anagrams_list


def list_manipulation(s):
    """
    To transform the input word 's' to list form
    """
    s_list = []
    for ch in s:
        s_list.append(ch)
    return s_list


def all_nums_list(s_list, c_word, all_list):
    if len(c_word) == len(s_list):
        all_list.append(c_word)
    else:
        # to get all permutations -> based on the numbers (順序) to represent each character
        # (solve same characters problem)
        for i in range(len(s_list)):
            ch = str(i)
            if ch in c_word:
                pass
            else:
                c_word = c_word + ch
                # explore
                all_nums_list(s_list, c_word, all_list)
                # backtracking
                c_word = c_word[:len(c_word)-1]
    return all_list


def change_all_nums(all_nums, s_list):
    """
    To change all nums list to all words list
    """
    new_all_list = []
    for word in all_nums:
        # Transform numbers to a normal word
        word = transformer(word, s_list)
        if word in new_all_list:
            pass
        else:
            new_all_list.append(word)
    return new_all_list


def transformer(word, s_list):
    """
    To get each number in each word, and then get 字母順序 in s_list 做配對
    """
    x = ''
    for number in word:
        ch = s_list[int(number)]
        x = x + ch
        # if the word we input in the console is more than 8 characters, open the below programming
        """
        if not has_prefix(x):
            break
        """
    return x


def has_prefix(sub_s):
    """
    To early stop if we find the start of a word doesn't match all starts of the words in the dictionary
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
