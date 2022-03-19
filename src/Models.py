# Родительский Класс для всех Спрайтов
class Sprite:
    hp = 0          # Шкала здоровья
    armor = 0       # Броня
    speed = 0       # Скорость передвижения
    view_range = 0  # Дальность обзора
    level = 0       # Уровень
    live = True     # Живой/Мертвый

# Родительский Класс для всех видов оружия ближнего боя
class Simple_Weapon:
    def __init__(self, damage: int, range: int):
        self.damage = damage      # Урон
        self.range = range        # Дальность

# Родительский Класс для всех видов оружия дальнего боя
class Projectile_Weapon:
    def __init__(self, range: int, speed: int, damage: int, image: str):
        self.range = range       # Дальность полета
        self.speed = speed       # Скорость полета
        self.damage = damage     # Урон
        self.image = image       # Изображение снаряда