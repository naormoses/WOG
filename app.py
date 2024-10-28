import currency_roulette_game
import guess_game
import memory_game
from score import *

def welcome():
    username = input("Your Name: ")
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey!')

def start_play():
    
    print('Please choose a game to play:\n'
          '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n'
          '2. Guess Game - guess a number and see if you chose like the computer.\n'
          '3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
    
    chosen_game = int(input('Your Pick: '))
    while chosen_game > 3 or chosen_game < 1:
        chosen_game = int(input('Invalid input! Please enter a number corresponding to a game:'))

    

    difficulty = int(input('Please select the Difficulty between 1 and 5 you would like: '))
    while difficulty > 5 or difficulty < 1:
        difficulty = int(input('Invalid input! Please enter a number corresponding to a Difficulty:'))

    if chosen_game == 1:
        if memory_game.play(difficulty):
            add_Score(difficulty)
    elif chosen_game == 2:
        if guess_game.play(difficulty):
            add_Score(difficulty)
    elif chosen_game == 3:
        if currency_roulette_game.play(difficulty):
            add_Score(difficulty)


if __name__ == '__main__':
    start_play()