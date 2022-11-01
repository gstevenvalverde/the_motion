import ICommand
import Boy


class CommandDraw(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player, SCREEN):
        self.boy = player
        self.screen = SCREEN

    def execute(self):
        self.boy.draw(self.screen)
