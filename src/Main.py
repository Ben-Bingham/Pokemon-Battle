import sys, pygame, random
from pygame.math import Vector2
from Pokemon import Pokemon
from Battle import battleLoop

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Aerial", 20)

size = Vector2(450, 250)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Battle")

squirtle = Pokemon("Squirtle")
squirtle.renderable.position = Vector2(100, 125)

bulbasaur = Pokemon("Bulbasaur")
bulbasaur.renderable.position = Vector2(200, 125)

charmander = Pokemon("Charmander")
charmander.renderable.position = Vector2(300, 125)

selectedPokemon = -1

selectedCords = squirtle.renderable.position

winner = ""

# Game loop
while True:
    # Handle Events
    for event in pygame.event.get():
        # Exit Event
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    if (selectedCords == squirtle.renderable.position):
                        selectedCords = bulbasaur.renderable.position
                    elif (selectedCords == bulbasaur.renderable.position):
                        selectedCords = charmander.renderable.position
                    elif (selectedCords == charmander.renderable.position):
                        selectedCords = squirtle.renderable.position

                if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                    if (selectedCords == squirtle.renderable.position):
                        selectedCords = charmander.renderable.position
                    elif (selectedCords == bulbasaur.renderable.position):
                        selectedCords = squirtle.renderable.position
                    elif (selectedCords == charmander.renderable.position):
                        selectedCords = bulbasaur.renderable.position
                if event.key == pygame.K_RETURN:
                    if (selectedCords == squirtle.renderable.position):
                        selectedPokemon = 0
                    elif (selectedCords == bulbasaur.renderable.position):
                        selectedPokemon = 1
                    elif (selectedCords == charmander.renderable.position):
                        selectedPokemon = 2

    # Sky
    screen.fill((3, 190, 252))

    pygame.draw.rect(screen, (0, 0, 0), (selectedCords.x - 30, selectedCords.y - 30, 60, 60), border_radius=3)
    pygame.draw.rect(screen, (3, 190, 252), (selectedCords.x - 30 + 1, selectedCords.y - 30 + 1, 58, 58), border_radius=3)

    text = font.render("Please Select a Pokemon", True, (0, 0, 0))
    screen.blit(text, (50, 50))

    squirtle.renderable.draw(screen)
    bulbasaur.renderable.draw(screen)
    charmander.renderable.draw(screen)

    if (selectedPokemon >= 0):
        playerPokemon = ""
        if (selectedPokemon == 0):
            playerPokemon = squirtle
        elif (selectedPokemon == 1):
            playerPokemon = bulbasaur
        elif (selectedPokemon == 2):
            playerPokemon = charmander

        enemyPokemon = playerPokemon
        while (enemyPokemon == playerPokemon):
            val = random.randint(0, 2)
            if (val == 0):
                enemyPokemon = squirtle
            elif (val == 1):
                enemyPokemon = bulbasaur
            elif (val == 2):
                enemyPokemon = charmander

        winner = battleLoop(screen, size, playerPokemon, enemyPokemon)
        break

    pygame.display.flip()  

if (not winner.renderable.facingForward):
    winner.renderable.flip()

winner.renderable.position = Vector2(size.x / 2, size.y / 2)

while True:
    # Handle Events
    for event in pygame.event.get():
        # Exit Event
        if event.type == pygame.QUIT: 
            sys.exit()

    # Sky
    screen.fill((3, 190, 252))

    text = font.render(winner.name + " Wins!", True, (0, 0, 0))
    screen.blit(text, (50, 50))

    winner.renderable.draw(screen)

    pygame.display.flip()  

# Quit
pygame.quit()