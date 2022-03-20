"""
Здесь все собирается в единое целое!!!
"""
import pygame
from pygame.math import Vector2 as vec
import settings

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.game_stage = "main menu"
        pygame.display.set_caption("Pussy Knight")
        pygame.display.set_icon(pygame.image.load("assets/images/icon.bmp"))
        self.background = pygame.image.load("assets/images/background_live.gif")
        pygame.mixer.music.load("assets/music/LofiFruits-Gangsta'sParadise.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def load(self):
        self.background = pygame.image.load('assets/maps/pixil-frame-0.png')
        self.background = pygame.transform.scale(self.background, (settings.MAZE_WIDTH, settings.MAZE_HEIGHT))
        # Opening walls file
        # Creat walls list with co-ords of walls
        with open("../assets/walls/walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
        print(self.walls)

    def game_start(self):
        pass

    def main_menu(self):
        self.screen.blit(self.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        pygame.display.update()

    def run(self):
        while self.is_running:
            if self.game_stage == "main menu":
                self.main_menu()
        pygame.quit()