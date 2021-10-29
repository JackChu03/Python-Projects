"""
Name: Jack Chu
------------------------
TODO: To add up the numbers found in two ListNodes and create a new ListNode with the answer
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    head1 = l1
    head2 = l2
    lst1 = []
    lst2 = []
    # to get a list full of numbers found in l1
    while head1 is not None:
        lst1.append(head1.val)
        head1 = head1.next
    # transform the list to a string, and then transform the string to an int
    ans1 = ''
    for i in range(len(lst1)):
        ans1 = ans1 + str(lst1[-1-i])
    ans1 = int(ans1)
    # to get a list full of numbers found in l2
    while head2 is not None:
        lst2.append(head2.val)
        head2 = head2.next
    # transform the list to a string, and then transform the string to an int
    ans2 = ''
    for j in range(len(lst2)):
        ans2 = ans2 + str(lst2[-1-j])
    ans2 = int(ans2)
    # get the answer by adding two int form numbers
    ans = ans1 + ans2
    ans = str(ans)
    # To form a new ListNode contains the answer we want
    ans_head = ListNode(int(ans[-1]), None)
    cur = ans_head
    for i in range(len(ans)-1):
        cur.next = ListNode(int(ans[-1-i-1]), None)
        cur = cur.next
    cur.next = None
    return ans_head
    #######################
####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()


