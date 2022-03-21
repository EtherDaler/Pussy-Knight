import pygame
import math

from .Models import *

# Враги
class SimpleEnemy(Sprite):

    # Подсчет расстояния между ботом и игроком
    def get_dist(self, hero: object):
        return math.sqrt((self.coords[0] - hero.coords[0])**2 - (self.coords[1] - hero.coords[1])**2)

    # Лежат ли точки A B C на одной прямой
    # Проверяем через уравнение прямой
    def check_line(self, A, B, C):
        return (C[0]*(B[1] - A[1]) - C[1]*(B[0] - A[0])) == (A[0]*B[1] - A[1]*B[0])

    # Проверка видимости игрока ботом
    def check_hero(self, hero: object, walls: list):
        if self.get_dist(self, hero) <= self.view_range:
            for wall in walls:
                if self.check_line(self.coords, hero.coords, wall) is True:
                    return False
            return True
        return False

    # Бот обходит препятствия
    def get_around(self, walls: list):
        pass

    # Бот движется к игроку
    def move_to_hero(self, hero: object):
        pass

    # Бот атакует игрока
    def hero_atack(self, hero: object):
        pass

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
        pass

    def enemy_active(self, hero: object, walls: list, coords_start: tuple, coords_finish: tuple):
        if self.live is True:
            self.walk(coords_start, coords_finish)
            if self.check_hero(hero, walls) is True:
                self.get_around(walls)
                self.move_to_hero(hero)
                if self.hand is True:
                    self.hero_atack(hero)
                else:
                    self.hero_fire(hero)



