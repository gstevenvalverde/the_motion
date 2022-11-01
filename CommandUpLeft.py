import ICommand
import Boy


class CommandUpLeft(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.up_left()
