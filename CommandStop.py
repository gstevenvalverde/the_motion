import ICommand
import Boy


class CommandStop(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.stop()
