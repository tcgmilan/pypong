import pygame
from src import pypong

def main():
    print("PyPong By undefined024")
    game = pypong.PyPong()
    player_one = game.PlayerOne(input("What is the first player name: "))
    player_two = game.PlayerTwo(input("What is the second player name: "))
    game.play(player_one, player_two)

if __name__ == "__main__":
    main()
