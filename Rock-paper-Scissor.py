# hw1rsp.py
#
# Name(s): Khanh Nguyen
#
# Date: 09/10/15
#
#

import random  # it is for random function

user = raw_input("Choose your weapon: ")  # get the input from the user
comp = random.choice(['rock', 'paper', 'scissors'])

print 'the user (you) chose', user  # whatever user picks
print 'the comp (I) chose', comp  # whatever comp picks

# first case
if user == 'rock':  # the user picks rock
    if comp == 'rock': # then computer picks rock
        print "Draw" # then there will be draw
    elif comp == 'paper': #
        print "Computer Wins" #
    else:
        print "User Wins" #

# second case
elif user == 'paper':  # if user pick paper, then user will win
    if comp == 'rock':  #
        print "User win"  #
    elif comp == 'paper':  #
        print "Draw"  #
    else:
        print 'Computer Wins'  #
# third case

elif user == 'scissors':
    if comp == 'rock':
        print "computer wins"
    elif comp == 'paper':
        print 'User Wins'
    else:
        print "Draw"








