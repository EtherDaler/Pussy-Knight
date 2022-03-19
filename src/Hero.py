import pygame
from Models import Sprite, Simple_Weapon, Projectile_Weapon

class Knight(Sprite):
    weapon = None   # Оружие
    xp = 0          # Опыт
    kills = 0       # Убийства
    xp_need = 0     # Необходимо опыта, чтобы перейти на следущий уровень

    def __init__(self, hp=100, armor=1, speed=10, level=1, live=True, damage=15, range=5):
        self.hp = hp + (hp * level // 10)
        self.armor = armor + (armor * level // 13)
        self.speed = speed + (speed * level // 20)
        self.level = level
        self.live = live
        self.weapon = Simple_Weapon(damage + (damage * level // 10), range)
        self.xp_need = level * 200

    # Повышение уровня
    def level_up(self):
        self.level += 1
        self.xp = 0
        self.hp += self.hp * self.level // 10
        self.armor += self.armor * self.level // 13
        self.speed += self.speed * self.level // 20
        self.weapon.damage += self.weapon.damage * self.level // 10
        self.xp_need = self.level * 200

    # Понижение уровня
    def level_down(self):
        self.level -= 1
        self.xp = 0
        self.hp -= self.hp * self.level // 10
        self.armor -= self.armor * self.level // 13
        self.speed -= self.speed * self.level // 20
        self.weapon.damage -= self.weapon.damage * self.level // 10
        self.xp_need = self.xp_need // 200

    # Получить данный уровень игрока
    def get_level(self):
        return self.level

    # Добавить опыта
    def add_xp(self, score: int):
        self.xp += score
        if self.xp == self.xp_need:
            self.level_up()

    # Получит информацию о том, сколько опыта не хватает для перехода на новый уровень
    def delta_xp(self):
        return self.xp_need - self.xp

    # Увеличить счетчик убийств
    def kill(self):
        self.kills += 1
