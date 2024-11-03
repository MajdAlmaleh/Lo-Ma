# game.py
import pygame
from grid import NegativeMagnet, PositiveMagnet
from levels import load_levels
from config import *
from ui import draw_menu

class Game:
    def __init__(self):
        self.levels = load_levels()
        self.current_level = None
        self.selected_piece = None
        self.selected_target = None
        self.in_menu = True
        self.game_over = False
        self.game_won = False
        self.negative_magnet_index = None
        self.positive_magnet_index = None
        self.selected_level= None

    def reset_level(self, level_index):
        self.selected_level= level_index
        self.current_level = self.levels[level_index]
        self.current_level.reset()
        self.selected_piece = None
        self.selected_target = None
        self.game_over = False
        self.game_won = False
    
    def first_sequence_from_tuples(self, tuple_list, index, top_bottom=False):
        first_items = [t[index] for t in tuple_list]

        print(first_items)
        if not first_items:
            return []

        sequence = []

        sequence.append(first_items[-1])
        for i in range(len(first_items) - 2, -1, -1):
            if top_bottom:  
                if first_items[i] == first_items[i + 1] - 1:  
                    sequence.insert(0, first_items[i])
                else:
                    break

            else:
                if first_items[i] == first_items[i + 1] + 1:  
                    sequence.insert(0, first_items[i])
                else:
                    break



        sequenced_tuples = [t for t in tuple_list if t[index] in sequence]
        return sequenced_tuples







    def _shift_magnets_in_line(self, target_row, target_col, is_row=True):
        magnets_in_line = (
            self.current_level.grid.get_magnets_in_row(target_row) if is_row
            else self.current_level.grid.get_magnets_in_col(target_col)
        )
    
        item_to_remove = (target_row, target_col, self.current_level.grid.grid[target_row][target_col])
    
        items_right_up = []
        items_left_down = []
        
        for magnet in magnets_in_line:
            if is_row:
                if magnet[1] > item_to_remove[1]:
                    items_right_up.append(magnet)
                elif magnet[1] < item_to_remove[1]:
                    items_left_down.append(magnet)
            else:
                if magnet[0] > item_to_remove[0]:
                    items_left_down.append(magnet)
                elif magnet[0] < item_to_remove[0]:
                    items_right_up.append(magnet)
    
        if isinstance(item_to_remove[2], NegativeMagnet):
            magnets_in_line = (
                self.first_sequence_from_tuples(items_right_up, 1) +
                self.first_sequence_from_tuples(items_left_down[::-1], 1, top_bottom=True)
                if is_row else
                self.first_sequence_from_tuples(items_right_up[::-1], 0, top_bottom=True) +
                self.first_sequence_from_tuples(items_left_down, 0)
            )
        elif isinstance(item_to_remove[2], PositiveMagnet):
            magnets_in_line = (
                items_right_up[::-1] + items_left_down if is_row
                else items_right_up + items_left_down[::-1]
            )
    
        shift_group = []
        for magnet in magnets_in_line:
            if magnet == item_to_remove:
                continue
            mag_row, mag_col = magnet[0], magnet[1]
            if isinstance(item_to_remove[2], NegativeMagnet):
                move_offset = -1 if (mag_col if is_row else mag_row) < (target_col if is_row else target_row) else 1
            else:
                move_offset = 1 if (mag_col if is_row else mag_row) < (target_col if is_row else target_row) else -1
    
            new_row = mag_row + move_offset if not is_row else mag_row
            new_col = mag_col + move_offset if is_row else mag_col
    
            if 0 <= new_row < self.current_level.grid.rows and 0 <= new_col < self.current_level.grid.cols:
                shift_group.append((mag_row, mag_col, new_row, new_col))
    
        for mag_row, mag_col, new_row, new_col in shift_group:
            self.current_level.grid.move_magnet(mag_row, mag_col, new_row, new_col)
    

    def move_item(self):
        old_row, old_col = self.selected_piece
        target_row, target_col = self.selected_target
    
        if not self.current_level.grid.is_cell_empty(target_row, target_col):
            self.selected_target = None
            return
    
        self.current_level.grid.move_magnet(old_row, old_col, target_row, target_col)
    
        self._shift_magnets_in_line(target_row, target_col, is_row=True)
        self._shift_magnets_in_line(target_row, target_col, is_row=False)
    
        self.current_level.remaining_moves -= 1
        self.selected_piece = None
        self.selected_target = None
    
        print("Grid state")
        self.current_level.grid.print_grid_state()
    
        if self.current_level.grid.check_win():
            self.game_won = True
            print("You win!")
        elif self.current_level.remaining_moves <= 0:
            self.game_over = True

    def draw(self):
        if self.in_menu:
            draw_menu()  
        else:
            SCREEN.fill(BACKGROUND_COLOR)
            self.current_level.grid.draw(selected_piece=self.selected_piece, selected_target=self.selected_target)

            font = pygame.font.Font(None, 36)
            move_text = font.render(f"Moves left: {self.current_level.remaining_moves}", True, (255, 255, 255))
            SCREEN.blit(move_text, (10, 10))

