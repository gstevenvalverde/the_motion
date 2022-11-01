import ICommand
import Boy


class CommandUpRight(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.up_right()
