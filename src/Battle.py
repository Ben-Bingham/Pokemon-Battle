import pygame, sys
from pygame.math import Vector2

pygame.font.init()

font = pygame.font.SysFont("Aerial", 15)
margin = 10

def drawStatusBoxs(screen, size, pokemon, pos):
    boxColour = (235, 244, 245)
    fontColour = (0, 0, 0)
    borderColour = (0, 0, 0)

    pygame.draw.rect(screen, borderColour, (pos.x + margin - 2, pos.y + margin - 2, size.x / 3 + 4, size.y / 5 + 4), border_radius=3)
    pygame.draw.rect(screen, boxColour, (pos.x + margin, pos.y + margin, size.x / 3, size.y / 5))

    name = font.render(pokemon.name, True, fontColour)
    screen.blit(name, (pos.x + 20, pos.y + 20))

    hpText = font.render("HP:", True, fontColour)
    screen.blit(hpText, (pos.x + 20, pos.y + 40))

    pygame.draw.rect(screen, borderColour, (pos.x + margin * 2 + 20, pos.y + margin * 4, (size.x / 3) / 2, 10), border_radius = 5)
    if (pokemon.hp == pokemon.maxHp):
        pygame.draw.rect(screen, (0, 255, 0), (pos.x + margin * 2 + 2 + 20, pos.y + margin * 4 + 2, (size.x / 3) / 2 - 4, 10 - 4), border_radius = 5)
    else:
        colour = (0, 255, 0)
        percentageFull = pokemon.hp / pokemon.maxHp
        if (percentageFull < 0.5):
            colour = (255, 127, 0)
        elif (percentageFull < 0.25):
            colour = (255, 0, 0)

        pygame.draw.rect(screen, colour, (pos.x + margin * 2 + 2 + 20, pos.y + margin * 4 + 2, ((size.x / 3) / 2 - 4) * percentageFull, 10 - 4), border_top_left_radius=5, border_bottom_left_radius=5)

def drawMoveSelection(screen, size, activePokemon):
    boxColour = (235, 244, 245)
    fontColour = (0, 0, 0)
    borderColour = (0, 0, 0)

    pygame.draw.rect(screen, borderColour, (0, size.y / 4 * 3 + 1, size.x, size.y / 4))
    pygame.draw.rect(screen, boxColour, (2, size.y / 4 * 3 + 2 + 1, size.x - 4, size.y / 4 - 4))

    i = 0
    for move in activePokemon.moves:
        moveName = font.render(move.name, True, fontColour)
        x = margin + size.x / 3 * 2
        if (i > 1):
            x += 50
        
        y = (size.y / 4) * 3 + margin
        if (i % 2 == 1):
            y = (size.y / 4) * 3 + margin + 20

        screen.blit(moveName, (x, y))
        i += 1

def drawMessage(screen, size, message):
    fontColour = (0, 0, 0)
    if (len(message) < 50):
        messageText = font.render(message, True, fontColour)
        screen.blit(messageText, (margin, (size.y / 4) * 3 + margin))
    else:
        messageText1 = font.render(message[0:50], True, fontColour)
        screen.blit(messageText1, (margin, (size.y / 4) * 3 + margin))
        messageText2 = font.render(message[50:], True, fontColour)
        screen.blit(messageText2, (margin, (size.y / 4) * 3 + margin + 20))

def battleLoop(screen, size, lPokemon, rPokemon):
    leftPokeSpot = Vector2(size.x / 3, size.y / 3 * 2)
    rightPokeSpot = Vector2(size.x / 3 * 2, size.y / 3)

    lPokemon.renderable.position = leftPokeSpot
    lPokemon.renderable.facingForward = False

    rPokemon.renderable.position = rightPokeSpot
    rPokemon.renderable.facingForward = True

    activePokemon = lPokemon

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        screen.fill((0, 255, 0))

        lPokemon.renderable.draw(screen)
        rPokemon.renderable.draw(screen)

        drawStatusBoxs(screen, size, lPokemon, Vector2(0, 0))
        drawStatusBoxs(screen, size, rPokemon, Vector2(size.x / 2, size.y / 2))

        drawMoveSelection(screen, size, activePokemon)

        drawMessage(screen, size, "Squirtle has been scratcd and has now fainted. Lorem Ipsum fake text greek is weird klashjdfajsdf;klajdf;l")

        pygame.display.flip()
