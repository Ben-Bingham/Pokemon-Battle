import sys, pygame
from pygame.math import Vector2
from Pokemon import Pokemon

pygame.init()

# Game Setup
size = width, height = 450, 250

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Battle")

squirtle = Pokemon("assets/images/Squirtle_Front.png", "assets/images/Squirtle_Back.png")
squirtle.renderable.position = Vector2(100, 125)

bulbasaur = Pokemon("assets/images/Bulbasaur_Front.png", "assets/images/Bulbasaur_Back.png")
bulbasaur.renderable.position = Vector2(200, 125)

charmander = Pokemon("assets/images/Charmander_Front.png", "assets/images/Charmander_Back.png")
charmander.renderable.position = Vector2(300, 125)

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