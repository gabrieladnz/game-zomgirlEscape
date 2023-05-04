from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

# inicializa o morcego
class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        # posição inicial na tela
        self.rect.y = 180
        self.step_index = 0
    
    # desenha ele na tela
    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0
