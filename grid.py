# grid.py
import pygame
from config import *

class Magnet:
    id_counter = 0
    def __init__(self, magnet_type):
        self.magnet_type = magnet_type
        self.id = Magnet.id_counter
        Magnet.id_counter += 1


    def draw(self, rect):
        center = rect.center
        radius = (rect.width // 2) - 10

        if self.magnet_type == '+':
            color = POSITIVE_MAGNET_COLOR
        elif self.magnet_type == '-':
            color = NEGATIVE_MAGNET_COLOR
        else:
            color = NORNMAL_MAGNET_COLOR

        pygame.draw.circle(SCREEN, color, center, radius)

class PositiveMagnet(Magnet):
    def __init__(self):
        super().__init__('+')

class NegativeMagnet(Magnet):
    def __init__(self):
        super().__init__('-')

class NormalMagnet(Magnet):
    def __init__(self):
        super().__init__('0')


class Grid:
    def __init__(self, initial_state, fixed_cells):
        self.rows = len(initial_state)
        self.cols = len(initial_state[0]) if self.rows > 0 else 0
        self.cell_size = self.calculate_cell_size(self.cols * self.rows)
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.initial_state = initial_state
        self.fixed_cells = fixed_cells
        self.load_initial_state()


    def calculate_cell_size(self, total_cells):
        if total_cells <= 12:
            return 100
        elif total_cells <= 25: 
                return 75
        elif total_cells <= 36: 
                return 75
        else: return 50
    

    def get_magnets_in_row(self, row,reversed=True):
        if reversed:
            return [(row, col, self.grid[row][col]) for col in range(self.cols - 1, -1, -1) if self.grid[row][col] is not None]
        else:
            return [(row, col, self.grid[row][col]) for col in range(self.cols) if self.grid[row][col] is not None]
    
    def get_magnets_in_col(self, col,reversed=True):
        if reversed:
            return [(row, col, self.grid[row][col]) for row in range(self.rows -1 ,-1, -1) if self.grid[row][col] is not None]
        else:
            return [(row, col, self.grid[row][col]) for row in range(self.rows) if self.grid[row][col] is not None]

    def load_initial_state(self):
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.initial_state[row][col] == 1:
                    self.grid[row][col] = PositiveMagnet()
                elif self.initial_state[row][col] == 2:
                    self.grid[row][col] = NegativeMagnet()
                elif self.initial_state[row][col] == 3:
                    self.grid[row][col] = NormalMagnet()


    def find_magnet_type(self,type):
        magnets = [
                        (row, col) for row in range(self.rows)
                        for col in range(self.cols)
                        if isinstance(self.grid[row][col], type)
                    ]
        return magnets
 

    def print_grid_state(self):
        state_repr = []
        for row in self.grid:
            row_repr = []
            for cell in row:
                if isinstance(cell, PositiveMagnet):
                    row_repr.append("+")
                elif isinstance(cell, NegativeMagnet):
                    row_repr.append("-")
                elif isinstance(cell, NormalMagnet):
                    row_repr.append("0")
                elif (row,cell) in self.fixed_cells:
                    row_repr.append("1")
                else:
                    row_repr.append(" ")
            state_repr.append(" | ".join(row_repr))
        print("\n".join(state_repr))
        print("-" * 20)


    def draw(self, selected_piece=None, selected_target=None):
        margin = 10  
        circle_radius = (self.cell_size - margin) // 2  

        total_width = self.cols * self.cell_size
        total_height = self.rows * self.cell_size

        offset_x = (SCREEN.get_width() - total_width) // 2
        offset_y = (SCREEN.get_height() - total_height) // 2

        for row in range(self.rows):
            for col in range(self.cols):
                x = offset_x + col * self.cell_size + self.cell_size // 2
                y = offset_y + row * self.cell_size + self.cell_size // 2

                is_fixed_cell = (row, col) in self.fixed_cells
                color = FIXED_CELL_COLOR if is_fixed_cell else GRID_COLOR  

                pygame.draw.circle(SCREEN, color, (x, y), circle_radius)

                magnet = self.grid[row][col]
                if magnet:
                    magnet_rect = pygame.Rect(x - circle_radius, y - circle_radius, 2 * circle_radius, 2 * circle_radius)
                    magnet.draw(magnet_rect)

                if (row, col) == selected_piece:
                    pygame.draw.circle(SCREEN, SELECTED_COLOR, (x, y), circle_radius + 2, 3)
                elif (row, col) == selected_target:
                    pygame.draw.circle(SCREEN, SELECTED_COLOR, (x, y), circle_radius + 4, 5)


    def is_cell_empty(self, row, col):
        return self.grid[row][col] is None

    def move_magnet(self, old_row, old_col, new_row, new_col):
        if self.grid[new_row][new_col] is None:
            self.grid[new_row][new_col] = self.grid[old_row][old_col]
            self.grid[old_row][old_col] = None

    def check_win(self):
        for row, col in self.fixed_cells:
            if self.grid[row][col] is None:
                return False
        return True


class Level:
    def __init__(self, grid, max_moves):
        self.grid = grid
        self.max_moves = max_moves
        self.remaining_moves = max_moves

    def reset(self):
        self.grid.load_initial_state()
        self.remaining_moves = self.max_moves