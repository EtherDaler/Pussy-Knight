import pygame
import math

from Models import Sprite, Simple_Weapon, Projectile_Weapon

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

