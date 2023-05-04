import pygame
import pygame.font
# importando constantes
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager

# classe principal do jogo
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        # pontuação
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        # localização
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        # objetos do jogo
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

# método que inicializa o jogo e seu loop inicial
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                # exibe o jogo na tela
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

 # método que inicia o movimento no jogo
    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        # inicia a velocidade e a pontuação
        self.game_speed = 20
        self.score = 0
        # jogo rodando
        while self.playing:
            # atualiza o estado do jogo
            self.events()
            self.update()
            self.draw()

# recebendo as interações do usuário
    def events(self):
        for event in pygame.event.get():
            # QUIT permite fechar a janela e encerrar o loop
            if event.type == pygame.QUIT:
                # iniciar
                self.playing = False
                # caminhar
                self.running = False

# atualizar informações do jogo a cada partida
    def update(self):
        # captura a tecla pressionada
        user_input = pygame.key.get_pressed()
        # atualiza posição do personagem
        self.player.update(user_input)
        # obstáculo
        self.obstacle_manager.update(self)
        # pontuação
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
    
    # método que atualiza a pontuação e aumenta velocidade do jogo
    def update_score(self):
        self.score += 1
        # a cada 100 pontos a velocidade aumenta em 2
        if self.score % 100 == 0:
            self.game_speed += 2

    # método que desenha os elementos na tela
    def draw(self):
        # controla a velocidade a partir do FPS
        self.clock.tick(FPS)
        # cor da tela
        self.screen.fill((255, 255, 255))
        # fundo do jogo
        self.draw_background()
        # exibe o personagem jogador
        self.player.draw(self.screen)
        # exibe os obstáculos 
        self.obstacle_manager.draw(self.screen)
        # exibe a pontuação
        self.draw_score()
        # tempo do power_up na tela
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        
        # atualiza os elementos alterados
        pygame.display.update()
        # atualiza a tela inteira
        pygame.display.flip()
    
    # método que desenha o fundo do jogo
    def draw_background(self):
        self.screen.fill((0, 0, 0, 255))
        image_width = BG.get_width()
        # efeito de movimento no fundo do jogo
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed
    
    # método que exibe a mensagem de pontuação no fim do jogo
    def draw_score(self):
        draw_message_component(
            f"pontos: {self.score}",
            self.screen,
            # posição da mensagem na tela
            pos_x_center = 1000,
            pos_y_center = 50
        )
    
    # exibe o tempo do power na tela, caso o jogador tenha um
    def draw_power_up_time(self):
        # verifica se o jogador tem algum power
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
                
    # método que captura os eventos na tela de menu(sair, iniciar o jogo)
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            # clicar pra sair
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            # tecla pressionada pra iniciar
            elif event.type == pygame.KEYDOWN:
                self.run()

    # menu inicial do jogo
    def show_menu(self):
        # cor do menu
        self.screen.fill((235, 156, 243))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        # mensagens exibidas no menu
        if self.death_count == 0:
            draw_message_component("Olá! Pressione qualquer tecla pra iniciar o jogo.", self.screen, font_color=(255, 255, 255))
        else:
            draw_message_component("Pressione qualquer tecla para reiniciar o jogo.", self.screen, font_color=(255, 255, 255), pos_y_center = half_screen_height + 140)
            draw_message_component(
                f"Sua pontuação: {self.score}",
                self.screen,
                font_color=(255, 255, 255),
                pos_y_center=half_screen_height - 180
            )

            draw_message_component(
                f"Tentativas: {self.death_count}",
                self.screen,
                font_color=(255, 255, 255),
                pos_y_center=half_screen_height - 100
                )
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 30))
        
        #atualizando a tela
        pygame.display.flip()
        self.handle_events_on_menu()
