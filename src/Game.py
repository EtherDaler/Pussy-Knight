"""
Здесь все собирается в единое целое!!!
"""
import pygame
import random

class Game:
    def __init__(self):
        self.WIDTH = 520  # ширина игрового окна
        self.HEIGHT = 800  # высота игрового окна
        self.FPS = 60  # частота кадров в секунду
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.game_stage = "main menu"
        pygame.display.set_caption("Pussy Knight")
        pygame.display.set_icon(pygame.image.load("assets/images/icon.bmp"))
        self.background = pygame.image.load("assets/images/background_live.gif")
        pygame.mixer.music.load("assets/music/LofiFruits-Gangsta'sParadise.wav")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

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