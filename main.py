"""
Отсюда запускается игра!!!
"""
import pygame
from src.Game import Game

pygame.init()


def main():
    my_game = Game()
    my_game.run()


if __name__ == '__main__':
    main()