import pygame
import os
from pygame.locals import *
from random import randrange

def check_position():
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
                    moving = False
                    print(f'Position: {event.pos}') # working get postion on a movable crosshair