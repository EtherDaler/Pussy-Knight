import pygame
from Models import Sprite, Simple_Weapon, Projectile_Weapon

class Boss(Sprite):
    hand = True     # Ближний бой
    weapon = None   # Оружие
    name = None     # Имя

    def __init__(self, name=None, hp=30, armor=0.5, speed=8, level=1, live=True,
                 hand=True, damage=8, range=5, p_speed=7, img=None):

        self.name = name
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

    """
    Тут будут реализованы способности босса!
    """