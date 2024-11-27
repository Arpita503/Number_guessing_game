from Day_01.art import logo
from random import randint

# Global variables

EASY_LEVE_TURNS=10
HARD_LEVE_TURNS=5

def check_answer(guess, answer, turns):
    #  check if our guess>answer: too high
    # if guess<answer: too low
    # Guess = answer : Guess is correct!
    if guess>answer:
        print("You've guessed too high!!")
        return turns -1
    elif guess<answer:
        print("You've guessed it too low!!")
        return turns-1
    else:
        print(f"You've guessed it correctly!!, The answer was {answer} Hurray!! you WON!")

# Setting the difficulty level
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard':  ")
    # either user if left with number of turns or turns are exhausted
    if level == "easy":
        return EASY_LEVE_TURNS
    else:
        return HARD_LEVE_TURNS

def game():
    print(logo)
    print("Welcome to Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100")
    #the final answer
    answer = randint(1, 100)
    #guess would be the guess user is making 
    guess = 0
    # turn has the number of attempts left for the user
    turns = set_difficulty()
    while guess!=answer:
        print(f"You have {turns} attempts remaining")
        guess = int(input("Make a guess: "))
        # turns, guess, answer
        # turns = 10, anaswer = 50, guess = 25
        # turns = 9
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You've run out of guesses, the number was {answer}!!")
            return
        elif guess!=answer:
            print("--Guess again--")

game()