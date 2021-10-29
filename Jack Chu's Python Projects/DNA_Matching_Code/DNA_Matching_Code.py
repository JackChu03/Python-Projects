"""
File: similarity.py
Name: Jack Chu
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    We first need to enter the long DNA sequence and the short DNA sequence
    to match, if the short sequence matches a part of the long sequence or
    the most similar part of the long sequence, then we get the best match,
    which is that part in the long DNA sequence.
    """
    long = input('Please give me a DNA sequence to search: ')
    short = input('What DNA sequence would you like to match? ')
    x = similar(long, short)
    print('The best match is '+x)


def similar(long, short):
    long = long.upper()
    short = short.upper()
    # case-insensitive
    if short in long:
        # to decide if short sequence is actually in the long DNA sequence
        return short
    else:
        k = ''
        max_len = len(k)
        for i in range(len(long) - len(short)+1):
            # the time that the short should be compared with those same-length parts in the long
            k = ''
            ans = long[i:i + len(short)]
            # the same-length part as the short in the long
            for j in range(len(short)):
                """
                knowing the length of short, we can know exactly the times that each letter of ans and short should 
                be compared with each other
                """
                if short[j] == ans[j]:
                    k = k + ans[j]
            if len(k) > max_len:
                max_len = len(k)
                # max_len means that we now have the most similar words(after comparing short and ans)
        for i in range(len(long) - len(short)+1):
            k = ''
            ans = long[i:i + len(short)]
            for j in range(len(short)):
                if short[j] == ans[j]:
                    k = k + ans[j]
            if len(k) == max_len:
                """
                Because we already know the max_len, we know when the most similar words happens,
                so we can thus get the ans we want(the most similar part compared with short in the long DNA sequence)
                """
                return ans




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()





