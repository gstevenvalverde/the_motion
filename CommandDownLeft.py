import ICommand
import Boy


class CommandDownLeft(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.down_left()
