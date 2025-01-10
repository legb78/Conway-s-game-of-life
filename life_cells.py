import numpy as np

class lifecells:
    def __init__(self, rows, cols):
   
        self.rows = rows
        self.cols = cols
        self.matrix = np.zeros((rows, cols), dtype=int)

    def set_initial_state(self, initial_state):
        
        self.matrix = np.array(initial_state)

    def analyse_cell(self, index_row, index_col):
        number_neighbors_alive = 0

        for row in range(index_row - 1, index_row + 2):
            for col in range(index_col - 1, index_col + 2):
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if row == index_row and col == index_col:
                        continue
                    if self.matrix[row][col] == 1:
                        number_neighbors_alive += 1

        return number_neighbors_alive








    def next_state(self):
        next_matrix = self.matrix.copy()

        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbors = self.analyse_cell(row, col)

                if self.matrix[row][col] == 0 and alive_neighbors == 3:
                    next_matrix[row][col] = 1
                elif self.matrix[row][col] == 1 and alive_neighbors in [2, 3]:
                    next_matrix[row][col] = 1
                else:
                    next_matrix[row][col] = 0

        self.matrix = next_matrix
