""" coins.py | Tue, Feb 07, 2017 | Roman S. Collins

    The problem:

    You place 100 coins heads up in a row and number them by position, with the coin all the way on the left No. 1 and the one on the rightmost edge
    No. 100. Next, for every number N, from 1 to 100, you flip over every coin whose position is a multiple of N. For example, first you'll flip over
    every coin whose position is a multiple of N. For example. First you'll flip over all the coins, because every number is a multiple of 1. Then you'll
    flip over all the even-numbered coins, because theyre multiples of 2. Then you'll flip coins No. 3, 6, 9, 12 and so on.

"""
def gen_coins(heads='.', n=100):
	for i in range(1, n + 1):
		coins = heads * n
	return coins

def flip_coins(coins, tails='·'):
    flipped_coins = []

    # Make list
    for c in range(len(coins)):
        flipped_coins.append(coins[c])

    print(flipped_coins)

    """
        for i in range(len(flipped_coins)):
            #print(i, end='')
            for n in range(len(flipped_coins)):
                if i == 0:
                    flipped_coins[i] = tails
                    try:
                        if n % i == 0:
                            flipped_coins[i] = tails
                            #print((n % i), end='')
                    except ZeroDivisionError:
                        pass
        print(''.join(flipped_coins))
    return ''.join(flipped_coins)
    """

    for n in range(len(coins)):
        print(flipped_coins[n])


def main():
	coins = gen_coins(heads = '+', n = 3)
	#print('')
	#print(coins)

	flipped_coins = flip_coins(coins, tails = '-')
	#print('')
	#print(flipped_coins)

if __name__ == '__main__':
    main()
