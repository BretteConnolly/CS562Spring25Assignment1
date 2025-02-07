#Brette Fitzgibbon

from random import randint

# MonteCarlo.py
# This program uses a Monte Carlo approach to estimate the probability of winning the dice game "Approach" with different
# "hold" values.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# Note:
# We can reduce this to the problem of player 1 choosing the best value at which to hold.
# This is called a policy; once we know the best number to hold at, we can act optimally.

# To estimate the best number to hold at, we'll try to estimate the probability of winning
# for each possible hold value between n-5 and n.
# Once we have this, we will know which hold value to use for our strategy.

# This function should try each possible hold value 1000000 times. For each time, play a random
# game. If Player 1 wins, increment the appropriate value in the win_table dictionary.

# n is the limit.

def monte_carlo_approach(n) :
    win_table = {}
    for i in range(n-5,n+1) :
        win_table[i] = 0

    for hold_val in range(n-5,n+1) :
        for i in range(1000000) :
        ## player 1 plays
            p1_total = 0
            while p1_total < hold_val: #while hold value as not been reached
                p1_total += randint(1,6) #dice roll
        ## player 1 done. Did they exceed n?
        ## if not, player 2 plays
            if p1_total <= n: #if p1 does not exceed the target, then player 2 plays
                p2_total = 0
                ## player 2 > player1?
                while p2_total <= p1_total and p2_total < n: #player 2 wants to exceed player 1, but not exceed the target
                    p2_total += randint(1,6) #dice roll
                if p2_total > n: #player 2 exceeds the target
                    win_table[hold_val] += 1 #player 1 wins
                #If player 1 and player 2 tie at the target, nobody wins

    for item in win_table.keys() :
        print("%d: %f" % (item, win_table[item]/1000000))