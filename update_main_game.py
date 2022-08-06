import sys

sys.path.insert(1, '..\\memoryGame')
from memory_game  import mem_play_diff
sys.path.insert(2, '..\\currencyRouletteGame')
from currency_rollete import currency_play_diff
sys.path.insert(3, '..\\guessGame')
from guess_game import guess_play_diff


def play_game():
    game=int(input("\nPleasee choose game \n1.GuessGame \n2. MemoryGame\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
    difficulty = int(input("Please choose difficulty to use for this game"))
    if game == 1:
        guess_play_diff(difficulty)
    if game == 2:
        mem_play_diff(difficulty)
    if game == 3:
        currency_play_diff(difficulty)


if __name__ == '__main__':
    play_game()

