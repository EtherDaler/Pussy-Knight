import pygame
from Models import Sprite, Simple_Weapon, Projectile_Weapon

# Враги
class SimpleEnemy(Sprite):
    hand = True     # Ближний бой
    weapon = None   # Оружие

    def __init__(self, hp=30, armor=0.5, speed=8, level=1, live=True, hand=True, damage=8, range=5, p_speed=7, img=None):
        self.hp = hp + (hp * level // 12)
        self.armor = armor + (armor * level // 15)
        self.speed = speed
        self.level = level
        self.live = live
        self.hand = hand
        # Выбор оружия в зависимости от типа боя
        if hand is True:
            self.weapon = Simple_Weapon(damage + (damage * level // 12), range)
        else:
            self.weapon = Projectile_Weapon(range, p_speed, damage + (damage * level // 12), img)

    def get_dist(self, hero):
        return abs((self.coords[0] - hero.coords[0])**2 - (self.coords[1] - hero.coords[1])**2)

    def check_hero(self, hero, map): # проверка видимости игрока
        if get_dist(self, hero)<=self.view_range**2:
            def block_on_line(self, hero, block):
                return False # проверка свободности линии, затычка
            if (1-sum([int(block_on_line(self, hero, block)) for block in map])):
                return True
        return False

    def attack(self, hero):
         