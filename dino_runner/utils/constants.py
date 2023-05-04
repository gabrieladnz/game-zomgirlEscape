import pygame
import os

# constantes globais contendo o título, tamanho de tela e imagens
TITLE = "Zomgirl Escape"
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 650
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# redimensionando imagem do ícone do jogo
new_size = (90, 150)
ICON = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "01.png")), new_size)

# imagens correspondentes a cada ação do personagem: correr, pular, abaixar...
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

# carregando imagem dos obstáculos do jogo
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zumbi3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zumbi3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zumbi3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zumbi1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zumbi2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zumbi1.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/morcego1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/morcego2.png")),
]

# imagens do cenário do jogo
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/espada.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/hammer.png'))

# alterando o tamanho da imagem da variável BG
# tam = (650, 400)
tam = (650, 400)
BG = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Cenário/fundo.png')), tam)

# carrega a imagem do coração
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Cenário/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
