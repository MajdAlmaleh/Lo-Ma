import pygame
from config import *
import time


def draw_menu(screen, levels):
    screen.fill(MENU_BACKGROUND)
    
    font = pygame.font.Font(None, 48)
    title = font.render("Select a Level", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH // 2, 100))
    screen.blit(title, title_rect)

    button_font = pygame.font.Font(None, 36)
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
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

        level_text = button_font.render(f"{i + 1}", True, (0, 0, 0))
        text_rect = level_text.get_rect(center=button_rect.center)
        screen.blit(level_text, text_rect)

def draw_game_screen(screen, game):
    screen.fill(BACKGROUND_COLOR)
    game.current_level.grid.draw(selected_piece=game.selected_piece, selected_target=game.selected_target)
    font = pygame.font.Font(None, 36)
    move_text = font.render(f"Level: {game.selected_level +1}", True, (255, 255, 255))
    screen.blit(move_text, (10, 10))
    move_text = font.render(f"Moves left: {game.current_level.remaining_moves}", True, (255, 255, 255))
    screen.blit(move_text, (10, 50))

    if game.game_over:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(1200)
        game.reset_level(game.selected_level)
    elif game.game_won:
        win_text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(1200)
        game.reset_level(game.selected_level +1)
