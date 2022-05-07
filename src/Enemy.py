import pygame
import math

from .Models import Sprite, Simple_Weapon, Projectile_Weapon
from . import settings


# Враги


class SimpleEnemy(Sprite):
    to = True
    p_start: tuple
    p_finish: tuple
    state = 1

    def find_path(self, point: list, walls: list):
        if self.coords[0] < point[0]:
            self.move_right(walls)
            self.animation_walk()
        else:
            self.move_left(walls)
            self.animation_walk()
        if self.coords[1] < point[1]:
            self.move_back(walls)
            self.animation_walk()
        else:
            self.move_front(walls)
            self.animation_walk()

    # Подсчет расстояния между ботом и игроком

    def get_dist(self, hero: object):
        return math.sqrt((self.coords[0] - hero.coords[0]) ** 2 + (self.coords[1] - hero.coords[1]) ** 2)

    # Лежит ли точка C  между A и B
    # Сеачала проверяем через уравнение прямой, что точки на одной прямой
    # Потом через скалярное произведение проверяем лежит ли C на отрезке [A B]
    def check_line(self, A, B, C):
        cell_width = settings.MAZE_WIDTH // 28
        cell_height = settings.MAZE_HEIGHT // 30
        A1 = [A[0] // cell_width, A[1] // cell_height]
        B1 = [B[0] // cell_width, B[1] // cell_height]
        on_line = (C[0] - A1[0]) * (B1[1] - A1[1]) - (B1[0] - A1[0]) * (C[1] - A1[1])
        between = (C[0] * C[0] * A1[0] * B1[0]) + (C[1] * C[1] * A1[1] * B1[1])
        return on_line == 0 and between <= 0

    # Проверка видимости игрока ботом
    def check_hero(self, hero: object, walls: list):
        if self.get_dist(hero) <= self.view_range:
            for wall in walls:
                if self.check_line(self.coords, hero.coords, wall) is True:
                    return False
            return True
        return False

    # Бот обходит препятствия
    def get_around(self, walls: list):
        pass

    # Бот движется к игроку
    def move_to_hero(self, hero: object, walls: list):
        self.find_path(hero.coords, walls)

    # Бот атакует игрока
    def hero_atack(self, hero: object):
        if self.get_dist(hero) <= self.weapon.range and self.sleep == 0:
            self.animation_atack()
            hero.get_damage(self.weapon.damage)
            self.sleep = self.p_speed
            self.state = 2
        elif self.sleep > 0:
            self.sleep -= 1

    # Бот Стреляет в игрока
    def hero_fire(self, hero: object):
        pass

    # Бот бродит по карте
    def walk(self, walls: list, coords_start: tuple, coords_finish: tuple):
        """
        :param walls: Список стен
        :param coords_start: Откуда враг начинает бродить
        :param coords_finish: До куда враг бродит
        Враг бродит циклично
        """
        if abs(self.coords[0] - coords_finish[0]) < 2 and abs(self.coords[1] - coords_finish[1]) < 2:
            self.to = False
        if abs(self.coords[0] - coords_start[0]) < 2 and abs(self.coords[1] - coords_start[1]) < 2:
            self.to = True
        if not self.to:
            self.find_path(coords_start, walls)
        else:
            self.find_path(coords_finish, walls)
        pass

    def enemy_active(self, hero: object, walls: list, coords_start: tuple, coords_finish: tuple):
        if self.live is True:
            self.draw(1)
            if self.check_hero(hero, walls) is True:
                self.get_around(walls)
                self.move_to_hero(hero, walls)
                if self.hand is True:
                    self.hero_atack(hero)
                else:
                    self.state = 1
                    self.hero_fire(hero)
            else:
                self.state = 1
                self.walk(walls, coords_start, coords_finish)
        else:
            self.state = 5
            hero.kill()
            del self
