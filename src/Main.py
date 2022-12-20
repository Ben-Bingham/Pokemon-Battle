import sys, pygame
from pygame.math import Vector2
from Pokemon import Pokemon
from Battle import battleLoop

pygame.init()
pygame.font.init()

size = Vector2(450, 250)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Battle")

squirtle = Pokemon("Squirtle")
squirtle.renderable.position = Vector2(100, 125)

bulbasaur = Pokemon("Bulbasaur")
bulbasaur.renderable.position = Vector2(200, 125)

charmander = Pokemon("Charmander")
charmander.renderable.position = Vector2(300, 125)

battleLoop(screen, size, squirtle, bulbasaur)

# Game loop
while True:
    # Handle Events
    for event in pygame.event.get():
        # Exit Event
        if event.type == pygame.QUIT: sys.exit()

    # Sky
    screen.fill((3, 190, 252))

    squirtle.renderable.draw(screen)
    bulbasaur.renderable.draw(screen)
    charmander.renderable.draw(screen)

    pygame.display.flip()  

# Quit
pygame.quit()