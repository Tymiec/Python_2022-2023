import pygame

def is_left_mouse_click():
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0] == True:
        return True