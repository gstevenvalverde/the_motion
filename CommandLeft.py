import ICommand
import Boy


class CommandLeft(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.left()
