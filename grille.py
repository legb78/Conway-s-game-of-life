import pygame

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def update_cells(self, frame):
     
        for row in range(self.rows):
            for col in range(self.columns):
                self.cells[row][col] = frame[row][col]

    def drawing(self, window):
   
        for row in range(self.rows):
            for col in range(self.columns):
                color = (0, 255, 0) if self.cells[row][col] else (55, 55, 55)
                pygame.draw.rect(
                    window,
                    color,
                    (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1),
                )
