from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

def load_game():
    game = int(input("\nPlease choose a game to play:"
           "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to) guess it back"
           "\n2. Guess Game - guess a number and see if you chose like the computer"
           "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
           "\nValue: "))
    if game not in range(1,4):
        print("Unsupported value for a game. Please, enter a value between 1-3.")
        exit(1)

    difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    if difficulty not in range(1,6):
        print("Unsupported value for difficulty. Please, enter a value between 1-5.")
        exit(1)

    result = False
    match game:
        case 1:
            result = MemoryGame(difficulty).play()
        case 2:
            result = GuessGame(difficulty).play()
        case 3:
            result = CurrencyRouletteGame(difficulty).play()

    if result:
        add_score(difficulty)