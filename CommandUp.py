import ICommand
import Boy


class CommandUp(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player

    def execute(self):
        self.boy.up()
