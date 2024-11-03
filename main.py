# main.py
import sys
import pygame
from config import FPS,SCREEN
from game import Game
from ui import draw_menu, draw_game_screen
from utils import *
from grid import *

pygame.init()
pygame.display.set_caption("Logic Magnets")

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            sys.exit()

        if game.in_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_level = check_menu_click(event.pos, game.levels)
                if selected_level is not None:
                    game.reset_level(selected_level)
                    game.in_menu = False
        else:
            handle_key_events(event,game)


    if game.in_menu:
        draw_menu(SCREEN, game.levels)
    else:
        draw_game_screen(SCREEN, game)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
