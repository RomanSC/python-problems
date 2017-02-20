""" regiments.py | Sun, Feb 12, 2017 | Roman S. Collins

    Six regiments each send a colonel, a lieutenant-colonel, a major, a captain, a lieutenant, and a sub-lieutenant to a parade.
    How may the 36 soldiers be arranged into a six by six formation such that no regiment is repeated in any row or column
    and no rank is repeated in any row or column?

    Easier place to start: wht if there are three regiments with three ranks and you need a 3 x 3 grid of the nine soldiers?
    Or four regiments and ranks and you want a 4 x 4

"""

ranks = ['', '', '', '', '', '']
soldiers = ''

for i in range(6):
     for x in range(6):
         print('. ', end='')
     print('')

