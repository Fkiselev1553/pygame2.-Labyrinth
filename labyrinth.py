import pygame
#screen width, height
WIDTH = 600
HEIGHT = 800
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#kletka
cell = 80
grid_width = WIDTH // cell
grid_height = HEIGHT // cell
#background
screen.fill(WHITE)
for i in range(grid_width):
        for j in range(grid_height):
                #rectangle = pygame.rect(i*cell, f*cell, cell, cell)
                pygame.draw.rect(screen,BLACK,pygame.Rect(i*cell, j*cell, cell, cell), 1)
pygame.display.flip
running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        break
pygame.quit()
