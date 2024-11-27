import pygame
from grid import NegativeMagnet, PositiveMagnet
from config import *

def check_menu_click(pos, levels):
    num_levels = len(levels)
    num_rows = (num_levels + GRID_COLUMNS - 1) // GRID_COLUMNS 

    start_x = (WIDTH - (GRID_COLUMNS * (BUTTON_WIDTH + BUTTON_SPACING) - BUTTON_SPACING)) // 2
    start_y = 200 

    for i in range(num_levels):
        row = i // GRID_COLUMNS
        col = i % GRID_COLUMNS
        x = start_x + col * (BUTTON_WIDTH + BUTTON_SPACING)
        y = start_y + row * (BUTTON_HEIGHT + BUTTON_SPACING)
        
        button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        if button_rect.collidepoint(pos):
            return i 
    return None


def handle_magnet_selection(magnet_type, game):
    if magnet_type == PositiveMagnet:
        game.negative_magnet_index = None
        magnet_index = 'positive_magnet_index'
    else:
        game.positive_magnet_index = None
        magnet_index = 'negative_magnet_index'
    
    magnets = game.current_level.grid.find_magnet_type(magnet_type)
    if magnets:
        current_index = getattr(game, magnet_index, None)
        new_index = 0 if current_index is None else (current_index + 1) % len(magnets)
        setattr(game, magnet_index, new_index)

        game.selected_piece = magnets[new_index]
        game.selected_target = game.selected_piece

def handle_key_events(event, game):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game.in_menu = True
        elif event.key == pygame.K_s:
            handle_magnet_selection(NegativeMagnet, game)
        elif event.key == pygame.K_a:
            handle_magnet_selection(PositiveMagnet, game)
        elif event.key == pygame.K_b:
            bfs_path = game.solve_bfs()
            print("BFS Solution Path:", bfs_path)
        elif event.key == pygame.K_d:
            dfs_path = game.solve_dfs()
            print("DFS Solution Path:", dfs_path)
        elif event.key == pygame.K_u:
            solution = game.solve_ucs()
        elif event.key == pygame.K_h:
            solution = game.solve_hill_climbing()
            if solution:
                print("Solution found:", solution)
            else:
                print("No solution exists.")       
        elif event.key == pygame.K_r:
            game.reset_level(game.selected_level)

        
        if game.selected_piece:
            move_direction = {
                pygame.K_UP: (-1, 0),
                pygame.K_DOWN: (1, 0),
                pygame.K_LEFT: (0, -1),
                pygame.K_RIGHT: (0, 1)
            }.get(event.key)

            if move_direction:
                row_move, col_move = move_direction
                max_row, max_col = game.current_level.grid.rows - 1, game.current_level.grid.cols - 1
                current_row, current_col = game.selected_target

                game.selected_target = (
                    max(0, min(current_row + row_move, max_row)),
                    max(0, min(current_col + col_move, max_col))
                )
        
        if event.key == pygame.K_RETURN and game.selected_piece and game.selected_target:
            game.move_item()
