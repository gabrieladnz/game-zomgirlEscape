import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
    
    # atualiza opção do obstáculo na tela
    def update(self, game_speed, obstacles):
        # direciona o objeto na direção oposta do personagem-jogador
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
    # desenha o obstáculo
    def draw (self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
