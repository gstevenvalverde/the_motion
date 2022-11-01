import ICommand

import CommandUp
import CommandDown
import CommandLeft
import CommandRight
import CommandUpLeft
import CommandUpRight
import CommandDownLeft
import CommandDownRight
import CommandStop

class Invoker:

    commands = []

    def __init__(self, player):
        # self.commands.append(c)
        self.commands[0] = CommandUp.CommandUp(player)
        self.commands[1] = CommandDown.CommandDown(player)
        self.commands[2] = CommandLeft.CommandLeft(player)
        self.commands[3] = CommandRight.CommandRight(player)
        self.commands[4] = CommandDownLeft.CommandDownLeft(player)
        self.commands[5] = CommandDownRight.CommandDownRight(player)
        self.commands[6] = CommandUpLeft.CommandUpLeft(player)
        self.commands[7] = CommandUpRight.CommandUpRight(player)

    def action(self, i):
        self.commands[i].execute()
