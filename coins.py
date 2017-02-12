""" coins.py | Tue, Feb 07, 2017 | Roman S. Collins

    The problem:

    You place 100 coins heads up in a row and number them by position, with the coin all the way on the left No. 1 and the one on the rightmost edge
    No. 100. Next, for every number N, from 1 to 100, you flip over every coin whose position is a multiple of N. For example, first you'll flip over
    every coin whose position is a multiple of N. For example. First you'll flip over all the coins, because every number is a multiple of 1. Then you'll
    flip over all the even-numbered coins, because theyre multiples of 2. Then you'll flip coins No. 3, 6, 9, 12 and so on.

"""
import termcolor

def flip_coins(n, all_flips=False):
    coins = [x for x in range(n + 1)]
    coins[0] = None
    coins.append(None)

    flip_coins = ['+' for i in range(n + 1)]
    flip_coins[0] = ''

    for n in range(1, len(coins) - 1):
        for z in range(1, n + 1):
            if (coins[n] % z == 0):
                flip_coins[n] = flip(flip_coins[n])
        if all_flips == True:
            print(''.join(flip_coins))
    if all_flips == False:
        print(''.join(flip_coins))

def flip(coin):
    if coin == '+':
        coin = '-'
    elif coin == '-':
        coin = '+'

    return coin

def also_interesting():
    # Mostly just saving for later
    # to test and see if solving the problem
    # may be faster with something kinda
    # like this
    for y in range(1, 101):
        #print(termcolor.colored('.', 'red'))
        print('Flip#{}: '.format(y), end='')

        #if (y != 1) or (y != 0):
        flip = [x for x in range(0, 101, y)]
        print(len(flip))
        print(flip)

def main():
    coins = flip_coins(100)

if __name__ == '__main__':
    main()
