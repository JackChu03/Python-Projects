"""
File: hangman.py
Name: Jack
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The player needs to guess a random word , and has required chances to guess the
    letter in it, if he guesses the letter right, he will retain his chances and the word will
    show a part of the answer(which he already guesses it right), if he guesses the letter wrong,
    he will lose one chance, and if the player is out of the chances, he is dead
    """
    x = random_word()
    all_not_know_ans = _(x)
    # we should first change the answer to all '-', ans the player can thus only know how many letters in the word
    print('The word looks like: ' + all_not_know_ans)
    print('You have ' + str(N_TURNS) + ' guesses left')
    y = input('Your guess: ')
    y = y.upper()
    while not y.isalpha() or len(y) > 1:
        # if what the player input is more than one and is not alpha, then illegal format
        print('illegal format.')
        y = input('Your guess: ')
        y = y.upper()
    print(if_y_in_x(y, x))


def _(x):
    # the way to change the answer to all '-'
    ans = ''
    for i in range(len(x)):
        ans = ans + "-"
    return ans


def if_y_in_x(y, x):
    current_ans = _(x)
    left = N_TURNS
    # left means if the player guesses wrong, how many chances to guess he left
    while True:
        if y in x:
            print('You are correct!')
            current_ans = replace(y, x, current_ans)
            # get new current answer if the player guesses the right letter
            if current_ans != x:
                print('The word looks like: ' + current_ans)
                print('You have ' + str(left) + ' guesses left.')
            else:
                return 'You win!!\nThe word was: ' + x
        else:
            print('There\' no ' + y + '\'s in the word.')
            left = left - 1
            # wrong guess, lose one chance
            if left != 0:
                print('The word looks like: ' + current_ans)
                print('You have ' + str(left) + ' guesses left.')
            else:
                # out of chances
                return 'You are completely hung : (\nThe word was: ' + x
        y = input('Your guess: ')
        y = y.upper()
        while not y.isalpha() or len(y) > 1:
            # if what the player input is more than one and is not alpha, then illegal format
            print('illegal format.')
            y = input('Your guess: ')
            y = y.upper()


def replace(y, x, current_ans):
    # the way to get the new current word
    ans = ''
    for i in range(len(x)):
        if x[i] == y:
            ans = ans + x[i]
        else:
            ans = ans + current_ans[i]
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
