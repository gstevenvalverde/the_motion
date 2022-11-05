import ICommand

import CommandUp
import CommandDown
import CommandLeft
import CommandRight
import CommandUpLeft
import CommandUpRight
import CommandDownLeft
import CommandDownRight

import CommandUpdate
import CommandDraw


class Invoker:

    commands = []

    def __init__(self, player, SCREEN):
        # self.commands.append(c)
        self.commands.append(CommandUp.CommandUp(player))
        self.commands.append(CommandDown.CommandDown(player))
        self.commands.append(CommandLeft.CommandLeft(player))
        self.commands.append(CommandRight.CommandRight(player))
        self.commands.append(CommandUpLeft.CommandUpLeft(player))
        self.commands.append(CommandUpRight.CommandUpRight(player))
        self.commands.append(CommandDownLeft.CommandDownLeft(player))
        self.commands.append(CommandDownRight.CommandDownRight(player))
        self.commands.append(CommandUpdate.CommandUpdate(player))
        self.commands.append(CommandDraw.CommandDraw(player, SCREEN))

    def action(self, command):
        self.commands[command].execute()
