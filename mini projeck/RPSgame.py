# Author: Laiba Roshan Ali
# Email: laibaroshankhan@gmail.com

import random

print ("****Welcome to RPS Game****")

name = input("Enter your name ")

print ("""
1. paper vs rock ----> paper
2. rock vs scissors ----> rock
3. scissors vs paper ----> scissors""")

options = ("rock", "paper" , "scissors")
player = None
computer = random.choice(options)

while True:
    player = input("Enter a choice(rock , paper , scissors)")

    while player not in options :
        player = input("Enter valid input")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    elif player == computer:
        print("Its a tie!")
    else:
        print("You Lose!")

    repeat = input("do you want to play again?")
    if repeat == "no":
        print("Game over")
        print("Thanks for playing")