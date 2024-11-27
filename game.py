# game.py
from collections import deque
import heapq
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


    def solve_bfs(self):
        initial_state = self._get_current_state()
        queue = deque([(initial_state, [])]) 
        visited = set()
        while queue:
            current_state, path = queue.popleft()
            if self._is_win_state(current_state):
                return path 
            if current_state in visited:
                continue
            visited.add(current_state)
            
            for move in self._generate_valid_moves(current_state):
                
                new_state = self._apply_move(current_state, move)
                if new_state not in visited:
                    
                    queue.append((new_state, path + [move]))
        
        return None 

    def solve_dfs(self,):
        initial_state = self._get_current_state()
        stack = [(initial_state, [])]  
        visited = set()
        
        while stack:
            current_state, path = stack.pop()
            if self._is_win_state(current_state):
                return path 
            
            if current_state in visited:
                continue
            visited.add(current_state)
            for move in self._generate_valid_moves(current_state):
                new_state = self._apply_move(current_state, move)
                if new_state not in visited:
                    stack.append((new_state, path + [move]))
        
        return None 
    



    def solve_hill_climbing(self):

        initial_state = self._get_current_state()
        current_state = initial_state
        current_path = []
        visited = set()
        
        while True:
            visited.add(current_state)
            
            if self._is_win_state(current_state):
                return current_path
            
            moves = self._generate_valid_moves(current_state)
            successors = [(move, self._apply_move(current_state, move)) for move in moves]
            
            scored_successors = [
                (self._heuristic(successor_state), move, successor_state)
                for move, successor_state in successors
                if successor_state not in visited
            ]
            
            scored_successors.sort(key=lambda x: x[0])
            
            if not scored_successors:
                return None
            
            _, best_move, best_state = scored_successors[0]
            
            current_state = best_state
            current_path.append(best_move)
    
    def _heuristic(self, state):

        self._set_state(state)
        grid = self.current_level.grid
        
        misplaced_magnets = 0
        for r in range(grid.rows):
            for c in range(grid.cols):
                cell = grid.grid[r][c]
                if isinstance(cell, (PositiveMagnet, NegativeMagnet)) and not grid.is_magnet_correct(r, c):
                    misplaced_magnets += 1
        
        return misplaced_magnets




   
    def solve_ucs(self):
        initial_state = self._get_current_state()
        print("Initial state:", initial_state) 
        priority_queue = []
        heapq.heappush(priority_queue, (0, initial_state, []))
        visited = set()

        while priority_queue:
            current_cost, current_state, path = heapq.heappop(priority_queue)

            if self._is_win_state(current_state):
                return path

            if current_state in visited:
                continue
            visited.add(current_state)

            for move in self._generate_valid_moves(current_state):
                print("Checking move:", move) 
                new_state = self._apply_move(current_state, move)
                print("New state:", new_state) 
                if new_state not in visited:
                    print('priority_queue')
                    print(priority_queue, (current_cost + 1, new_state, path + [move]))
                    print('priority_queue')
                    heapq.heappush(priority_queue, (current_cost + 1, new_state, path + [move]))

        return None




    def  _get_current_state(self):
        print(tuple(tuple(row) for row in self.current_level.grid.grid))
        return tuple(tuple(row) for row in self.current_level.grid.grid)
    
    def _is_win_state(self, state):
        self._set_state(state)
        return self.current_level.grid.check_win()

    def _set_state(self, state):
        for r, row in enumerate(state):
            for c, cell in enumerate(row):
                self.current_level.grid.grid[r][c] = cell
    
    def _generate_valid_moves(self, state):
        self._set_state(state)
        moves = []
        for r in range(self.current_level.grid.rows):
            for c in range(self.current_level.grid.cols):
                if isinstance(self.current_level.grid.grid[r][c], (PositiveMagnet, NegativeMagnet)):
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        target_row, target_col = r + dr, c + dc
                        if self._is_valid_move(r, c, target_row, target_col):
                            moves.append(((r, c), (target_row, target_col)))
        return moves

    def _apply_move(self, state, move):
        self._set_state(state)
        (r, c), (target_row, target_col) = move
        
        self.current_level.grid.move_magnet(r, c, target_row, target_col)
        self._shift_magnets_in_line(target_row, target_col, is_row=True)
        self._shift_magnets_in_line(target_row, target_col, is_row=False)
        
        self.draw()
        pygame.display.flip()
        # pygame.time.delay(50)  # Adjust this delay to control visualization speed
        
        return self._get_current_state()


    def _is_valid_move(self, row, col, target_row, target_col):
        if 0 <= target_row < self.current_level.grid.rows and 0 <= target_col < self.current_level.grid.cols:
            return self.current_level.grid.is_cell_empty(target_row, target_col)
        return False

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

