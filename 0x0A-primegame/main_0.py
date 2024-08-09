#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3]))) #ben wins
print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]))) #maria wins
print("Winner: {}".format(isWinner(0, [0]))) #no winner
print("Winner: {}".format(isWinner(-1, [10]))) #no winner
#print("Winner: {}".format(isWinner(10000, [...]))) #maria wins
