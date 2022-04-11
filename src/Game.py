"""
Здесь все собирается в единое целое!!!
"""
import pygame
from pygame.math import Vector2 as vec
from . import settings
from .Hero import *
from .Enemy import *

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
        self.avatar = pygame.image.load("assets/sprites/Soldier-Red.png").convert_alpha()
        self.player = Knight(self.avatar, [settings.WIDTH // 2, settings.HEIGHT // 2], 100, 12, 1, 10, 3, 50, 1, True, True, 0, 10, 10, 5, 0, None)
        self.walls = []
        self.anim_count = 0
        self.cell_width = MAZE_WIDTH // 28
        self.cell_height = MAZE_HEIGHT // 30
        self.enemys = [] # Массив с врагами

    # Загрузка карты и добавление стен
    def load(self):
        self.background = pygame.image.load('assets/maps/pixil-frame-0.png')
        self.background = pygame.transform.scale(self.background, (settings.MAZE_WIDTH, settings.MAZE_HEIGHT))
        # Opening walls file
        # Creat walls list with co-ords of walls
        with open("assets/walls/walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append((xidx, yidx))

    def draw_grid(self):
        for wall in self.walls:
            pygame.draw.rect(self.background, (12, 55, 163),
                             (wall[0] * self.cell_width, wall[1] * self.cell_height, self.cell_width
                              , self.cell_height))

    # Рисуем текст
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    # Отрисовка главного меню
    def start_draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_text('PUSH SPACE BAR', self.screen, [settings.WIDTH // 2, settings.HEIGHT // 2 - 50],
                       settings.START_TEXT_SIZE, (170, 132, 58), settings.START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [settings.WIDTH // 2, settings.HEIGHT // 2 + 50],
                       settings.START_TEXT_SIZE, (33, 137, 156), settings.START_FONT, centered=True)
        self.draw_text('HIGH SCORE', self.screen, [4, 0],
                       settings.START_TEXT_SIZE, (255, 255, 255), settings.START_FONT)
        pygame.display.update()

    # Варианты действий в главном меню
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.load()
                self.game_stage = 'playing'

    def start_update(self):
        pass

    # Главное меню
    def main_menu(self):
        self.start_events()
        self.start_update()
        self.start_draw()

    # Анимирование
    def animate(self, args, coords):
        if self.anim_count + 1 >= settings.FPS:
            self.anim_count = 0
        self.screen.blit(args[self.anim_count // (settings.FPS // len(args))], coords)
        self.anim_count += 1

    # Действия в игре
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def playing_update(self):
        pass

    # Отрисовка Игры
    def playing_draw(self):
        self.screen.fill(settings.BLACK)
        self.screen.blit(self.background, (settings.TOP_BOTTOM_BUFFER // 2, settings.TOP_BOTTOM_BUFFER // 2))
        self.draw_text(f'KILL: {self.player.kills}', self.screen, [10, 0], 18, settings.WHITE, settings.START_FONT)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move_front(self.walls)
            self.player.orientation = 0
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_DOWN]:
            self.player.move_back(self.walls)
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_RIGHT]:
            self.player.move_right(self.walls)
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_LEFT]:
            self.player.move_left(self.walls)
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.player.move_diag('+', '+')
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.player.move_diag('+', '-')
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.player.move_diag('-', '-')
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.player.move_diag('-', '+')
            self.animate(self.player.draw(3), tuple(self.player.coords))
        if keys[pygame.K_SPACE]:
            self.animate(self.player.draw(2), tuple(self.player.coords))
            # Пробегаемся по массиву врагов, чтобы нанести урон одному
            for enemy in self.enemys:
                if enemy.get_dist(self.player) <= self.player.weapon.range:
                    enemy.get_damage(self.player.weapon.damage)
                    break
        else:
            self.animate(self.player.draw(1), tuple(self.player.coords))

    # Игра
    def game(self):
        self.draw_grid()
        self.playing_events()
        self.playing_update()
        self.playing_draw()

    def run(self):
        while self.is_running:
            self.clock.tick(settings.FPS)
            if self.game_stage == "main menu":
                self.main_menu()
            elif self.game_stage == 'playing':
                self.game()
            else:
                self.is_running = False
            pygame.display.update()
        pygame.quit()