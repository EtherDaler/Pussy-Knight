from pygame.math import Vector2 as vec

# screen setting
WIDTH, HEIGHT = 520, 800
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER

# colour setting
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (170, 18, 48)

# font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'
# player setting
PLAYER_START_POS = vec(WIDTH // 2, HEIGHT // 2)
# mob setting

PX = 32