import pygame
from grille import Grid
from life_cells import *

# Configuration Pygame
black = (0, 0, 0)
white = (255, 255, 255)
grey = (29, 29, 29)
cell_size = 100
window_width = 700
window_height = 700

pygame.init()
pygame.display.set_caption("Le jeu de la vie")
icon_path = pygame.image.load('conways_game.png')
pygame.display.set_icon(icon_path)

# Création de la fenêtre
window = pygame.display.set_mode((window_width, window_height))

# Initialisation des objets Grid et Frame
grid = Grid(window_width, window_height, cell_size)
frame = lifecells(window_height // cell_size, window_width // cell_size)

# Définir l'état initial
initial_state = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
frame.set_initial_state(initial_state)

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculer l'état suivant
    frame.next_state()

    # Mettre à jour les cellules de la grille
    grid.update_cells(frame.matrix)

    # Dessiner la grille
    window.fill(grey)
    grid.drawing(window)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler la vitesse d'animation
    clock.tick(2)  # 2 images par seconde (ajustable)

pygame.quit()
