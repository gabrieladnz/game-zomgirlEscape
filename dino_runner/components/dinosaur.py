import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

# imagens do personagem
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

# posição horizontal inicial do personagem
X_POS = 80
# posição vertical inicial do personagem
Y_POS = 280
# posição agachado
Y_POS_DUCK = 310
# velocidade do salto
JUMP_VEL = 10


class Dinosaur(Sprite):
    def __init__(self):
        # atributos do personagem
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_jump_vel = JUMP_VEL
        self.setup_state()

    # estado inicial do personagem
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    # atualiza os dados do personagem
    def update(self, user_input):
        # opções de ações do usuário
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        # tecla de pular
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        # tecla de abaixar
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        # personagem volta a correr, caso nenhuma tecla tenha sido pressionada
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0

    # atualiza a imagem e a posição do personagem pra correr
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    # função de saltar
    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            # cria o efeito pro personagem dar o salto
            self.dino_rect.y -= self.dino_jump_vel * 2
            self.dino_jump_vel -= 0.8
        if self.dino_jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.dino_jump_vel = JUMP_VEL

    # função abaixar
    def duck(self):
        # diminui a velocidade da imagem
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.dino_duck = False

    # desenha a imagem do personagem atualizada na tela
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
