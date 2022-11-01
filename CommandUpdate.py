import ICommand
import Boy
import pygame


class CommandUpdate(ICommand.ICommand):
    boy: Boy.Boy()

    def __init__(self, player):
        self.boy = player


    def execute(self):
        self.boy.update()
