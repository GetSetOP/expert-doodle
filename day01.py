#Rock Paper Scissors
import sys
import random
from enum import Enum

playerchoice = input("1 for Rock\n2 for Paper\n3 for Scissors: ")
player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("You  Must Enter From 1 to 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)
print(" ")
print("You Chose " + playerchoice + ".")
print("Computer Chose" + computerchoice + ".")

if player ==1 and computer ==3:
    print("You Win!")
elif player ==2 and computer ==3:
    print("Computer Wins!")
elif player ==3 and computer ==3:
    print("Tie Match!")
if player ==1 and computer ==2:
    print("You Win!")
elif player ==2 and computer ==2:
    print("Tie Match!")
elif player ==3 and computer ==2:
    print("You Win!")
if player ==1 and computer ==1:
    print("Tie Match!")
elif player ==2 and computer ==1:
    print("Computer Wins!")
elif player ==3 and computer ==1:
    print("Computer Wins!")
