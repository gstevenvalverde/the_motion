import pygame
import Boy

import Invoker


class Game:
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self):
        self.player = Boy.Boy()
        self.invoker = Invoker.Invoker(self.player, self.SCREEN)

    def main(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()

        while run:

            for event in pygame.event.get():
                self.invoker.action(8)
                if event.type == pygame.QUIT:
                    run = False
                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_w]:
                    self.invoker.action(0)
                elif user_input[pygame.K_s]:
                    self.invoker.action(1)
                elif user_input[pygame.K_a]:
                    self.invoker.action(2)
                elif user_input[pygame.K_d]:
                    self.invoker.action(3)
                elif user_input[pygame.K_q]:
                    self.invoker.action(4)
                elif user_input[pygame.K_e]:
                    self.invoker.action(5)
                elif user_input[pygame.K_z]:
                    self.invoker.action(6)
                elif user_input[pygame.K_c]:
                    self.invoker.action(7)

            self.SCREEN.fill((255, 255, 255))

            self.invoker.action(9)

            clock.tick(30)
            pygame.display.update()



