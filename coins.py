""" coins.py | Tue, Feb 07, 2017 | Roman S. Collins

    The problem:

    You place 100 coins heads up in a row and number them by position, with the coin all the way on the left No. 1 and the one on the rightmost edge
    No. 100. Next, for every number N, from 1 to 100, you flip over every coin whose position is a multiple of N. For example, first you'll flip over
    every coin whose position is a multiple of N. For example. First you'll flip over all the coins, because every number is a multiple of 1. Then you'll
    flip over all the even-numbered coins, because theyre multiples of 2. Then you'll flip coins No. 3, 6, 9, 12 and so on.

"""
import time

def coin_flip(token, fill):
    # print 100 "coins"
    for i in range(1, 100 + 1):
        print(fill, end='')
    print('')
    # i becomes the function
    # in this unkown mathematical
    # expression
    for i in range(1, 100 + 1):
        # start flipping to heads
        for n in range(1, 100 + 1):
            if n % i == 0:
                print(token, end='')
            else:
                print(fill, end='')
        print('')
        time.sleep(0.005)

def main():
    token = '·'; fill = ' '

    coin_flip(token, fill)

if __name__ == '__main__':
    main()
