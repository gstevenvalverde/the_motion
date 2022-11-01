import pygame
import Boy
import CommandUpdate
import CommandDraw

import CommandUp
import CommandDown
import CommandLeft
import CommandRight
import CommandUpLeft
import CommandUpRight
import CommandDownLeft
import CommandDownRight
import CommandStop


class Game:
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self):
        self.player = Boy.Boy()
        self.CommandUpdate = CommandUpdate.CommandUpdate(self.player)
        self.CommandDraw = CommandDraw.CommandDraw(self.player, self.SCREEN)

        self.CommandUp = CommandUp.CommandUp(self.player)
        self.CommandDown = CommandDown.CommandDown(self.player)
        self.CommandLeft = CommandLeft.CommandLeft(self.player)
        self.CommandRight = CommandRight.CommandRight(self.player)
        self.CommandDownLeft = CommandDownLeft.CommandDownLeft(self.player)
        self.CommandDownRight = CommandDownRight.CommandDownRight(self.player)
        self.CommandUpLeft = CommandUpLeft.CommandUpLeft(self.player)
        self.CommandUpRight = CommandUpRight.CommandUpRight(self.player)
        self.CommandStop = CommandStop.CommandStop(self.player)

        # self.invoker_update = Invoker.Invoker(CommandUpdate)
        # self.invoker_draw = Invoker.Invoker(CommandDraw)

    def main(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()

        while run:

            for event in pygame.event.get():
                self.CommandUpdate.execute()
                if event.type == pygame.QUIT:
                    run = False
                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_w]:
                    self.CommandUp.execute()
                elif user_input[pygame.K_s]:
                    self.CommandDown.execute()
                elif user_input[pygame.K_a]:
                    self.CommandLeft.execute()
                elif user_input[pygame.K_d]:
                    self.CommandRight.execute()
                elif user_input[pygame.K_q]:
                    self.CommandUpLeft.execute()
                elif user_input[pygame.K_e]:
                    self.CommandUpRight.execute()
                elif user_input[pygame.K_z]:
                    self.CommandDownLeft.execute()
                elif user_input[pygame.K_c]:
                    self.CommandDownRight.execute()
                elif user_input[pygame.K_SPACE]:
                    self.CommandStop.execute()

            self.SCREEN.fill((255, 255, 255))

            self.CommandDraw.execute()

            clock.tick(30)
            pygame.display.update()



