import ICommand
import Boy


class CommandRight(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.right()
