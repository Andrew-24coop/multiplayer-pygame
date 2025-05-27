import random

# General
FPS = 60
WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)
SEED = random.randint(0, 255)
TILE_SIZE = 1
CHUNK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

MAIN_COLORS = {
    "ocean": (0, 0, 255),
    "sand": (194, 178, 128),
    "grass": (34, 139, 34),
    "forest": (0, 100, 0),
    "mountain": (139, 137, 137)
}

