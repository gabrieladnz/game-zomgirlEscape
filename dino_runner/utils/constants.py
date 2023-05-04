import pygame
import os

# Global Constants
TITLE = "Zomgirl Escape"
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 600
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
new_size = (90, 150)
ICON = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "01.png")), new_size)


RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/02.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/03.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/03.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/03.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/03.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/06.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/06.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/06.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/04.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/bitey1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/bitey2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/bitey1.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/morcego1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/morcego2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/hammer.png'))

tam = (650, 400)
BG = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Cenário/fundo.png')), tam)

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"