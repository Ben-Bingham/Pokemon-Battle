import pygame, sys, random
from pygame.math import Vector2

pygame.font.init()

font = pygame.font.SysFont("Aerial", 15)
margin = 10

lastMove = -1

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
        if (percentageFull < 0.5 and percentageFull > 0.25):
            colour = (255, 127, 0)
        elif (percentageFull <= 0.25):
            colour = (255, 0, 0)

        pygame.draw.rect(screen, colour, (pos.x + margin * 2 + 2 + 20, pos.y + margin * 4 + 2, max(((size.x / 3) / 2 - 4) * percentageFull, 0), 10 - 4), border_top_left_radius=5, border_bottom_left_radius=5)

def drawMoveSelection(screen, size, activePokemon):
    boxColour = (235, 244, 245)
    fontColour = (0, 0, 0)
    borderColour = (0, 0, 0)

    pygame.draw.rect(screen, borderColour, (0, size.y / 4 * 3 + 1, size.x, size.y / 4))
    pygame.draw.rect(screen, boxColour, (2, size.y / 4 * 3 + 2 + 1, size.x - 4, size.y / 4 - 4))

    i = 0
    for move in activePokemon.moves:
        x = margin + size.x / 3 * 2
        if (i > 1):
            x += 50
        
        y = (size.y / 4) * 3 + margin
        if (i % 2 == 1):
            y = (size.y / 4) * 3 + margin + 20

        if (move.selected):
            pygame.draw.rect(screen, borderColour, (x - 1, y - 1, 7 * len(move.name) + 2, 12))
            pygame.draw.rect(screen, boxColour, (x, y, 7 * len(move.name), 10))

        moveName = font.render(move.name, True, fontColour)
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

def lerp(input1, input2, dt):
    Output = (1 - dt) * input1 + dt * input2
    return Output

def epsilonEqual(val1, val2, epsilon):
    if (val1 == 60):
        pass
    if (abs(val1 - val2) <= epsilon):
        return True
    else:
        return False

def playMove(screen, move, attacker, target):
    target.getAttacked(move)
    progress = 0
    originalPos = attacker.renderable.position.copy()

    epsilon = 0.1

    movement1 = False
    movement2 = False
    movement3 = False
    movement4 = False

    while True:
        if (move.name == "Kick"):
            if (not movement1):
                attacker.renderable.position.x = lerp(originalPos.x, target.renderable.position.x + 100, progress/(60))
                attacker.renderable.position.y = lerp(originalPos.y, target.renderable.position.y - 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement1 = True
                    progress += epsilon
            elif (not movement2):
                attacker.renderable.position.x = lerp(target.renderable.position.x + 100, target.renderable.position.x + 25, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y - 100, target.renderable.position.y + 75, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement2 = True
                    progress += epsilon
            elif (not movement3):
                attacker.renderable.position.x = lerp(target.renderable.position.x + 25, target.renderable.position.x - 25, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y + 75, target.renderable.position.y - 75, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement3 = True
                    progress += epsilon
            elif (not movement4):
                attacker.renderable.position.x = lerp(target.renderable.position.x - 25, originalPos.x, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y - 75, originalPos.y, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement4 = True
                    progress += epsilon
                
            if (movement1 and movement2 and movement3 and movement4):
                break
        elif (move.name == "Punch"):
            if (not movement1):
                attacker.renderable.position.x = lerp(originalPos.x, target.renderable.position.x + 100, progress/(60))
                attacker.renderable.position.y = lerp(originalPos.y, target.renderable.position.y - 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement1 = True
                    progress += epsilon
            elif (not movement2):
                attacker.renderable.position.x = lerp(target.renderable.position.x + 100, target.renderable.position.x - 100, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y - 100, target.renderable.position.y + 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement2 = True
                    progress += epsilon
            elif (not movement3):
                attacker.renderable.position.x = lerp(target.renderable.position.x - 100, target.renderable.position.x + 100, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y + 100, target.renderable.position.y - 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement3 = True
                    progress += epsilon
            elif (not movement4):
                attacker.renderable.position.x = lerp(target.renderable.position.x + 100, originalPos.x, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y - 100, originalPos.y, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement4 = True
                    progress += epsilon
                
            if (movement1 and movement2 and movement3 and movement4):
                break
        elif (move.name == "Scratch"):
            if (not movement1):
                attacker.renderable.position.x = lerp(originalPos.x, target.renderable.position.x + 100, progress/(60))
                attacker.renderable.position.y = lerp(originalPos.y, target.renderable.position.y + 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement1 = True
                    progress += epsilon
            elif (not movement2):
                attacker.renderable.position.x = lerp(target.renderable.position.x + 100, target.renderable.position.x - 100, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y + 100, target.renderable.position.y - 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement2 = True
                    progress += epsilon
            elif (not movement3):
                attacker.renderable.position.x = lerp(target.renderable.position.x - 100, target.renderable.position.x + 100, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y - 100, target.renderable.position.y + 100, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement3 = True
                    progress += epsilon
            elif (not movement4):
                attacker.renderable.position.x = lerp(target.renderable.position.x + 100, originalPos.x, progress/(60))
                attacker.renderable.position.y = lerp(target.renderable.position.y + 100, originalPos.y, progress/(60))

                if (epsilonEqual(progress, 60, epsilon)):
                    movement4 = True
                    progress += epsilon
                
            if (movement1 and movement2 and movement3 and movement4):
                break
        screen.fill((0, 255, 0))

        attacker.renderable.draw(screen)
        target.renderable.draw(screen)

        pygame.display.flip()

        progress += epsilon
        if (epsilonEqual(progress, 61, epsilon)):
            progress = 0

def battleLoop(screen, size, lPokemon, rPokemon):
    leftPokeSpot = Vector2(size.x / 3, size.y / 3 * 2)
    rightPokeSpot = Vector2(size.x / 3 * 2, size.y / 3)

    lPokemon.renderable.position = leftPokeSpot
    lPokemon.renderable.facingForward = False

    rPokemon.renderable.position = rightPokeSpot
    rPokemon.renderable.facingForward = True

    activePokemon = lPokemon
    inactivePokemon = rPokemon

    selectedMove = 0
    moveToPlay = -1
    battleDone = False
    battleDoneCountup = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN and not battleDone:
                if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    selectedMove -= 1
                if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                    selectedMove += 1
                if event.key == pygame.K_RETURN:
                    moveToPlay = selectedMove

        if (battleDone):
            battleDoneCountup += 1
        if (battleDoneCountup >= 15000):
            return inactivePokemon

        if (selectedMove >= len(activePokemon.moves)):
            selectedMove = 0
        elif (selectedMove == -1):
            selectedMove = len(activePokemon.moves) - 1

        i = 0
        for move in activePokemon.moves:
            if (i == selectedMove):
                move.selected = True
            else:
                move.selected = False
            i += 1

        screen.fill((0, 255, 0))

        lPokemon.renderable.draw(screen)
        rPokemon.renderable.draw(screen)

        drawStatusBoxs(screen, size, lPokemon, Vector2(0, 0))
        drawStatusBoxs(screen, size, rPokemon, Vector2(size.x / 2, size.y / 2))

        drawMoveSelection(screen, size, activePokemon)

        if (activePokemon == rPokemon):
            playMove(screen, activePokemon.moves[random.randint(0, 2)], activePokemon, inactivePokemon)

            temp = inactivePokemon
            inactivePokemon = activePokemon
            activePokemon = temp

        global lastMove

        if (moveToPlay != -1):
            playMove(screen, activePokemon.moves[moveToPlay], activePokemon, inactivePokemon)
            lastMove = moveToPlay
            moveToPlay = -1

            temp = inactivePokemon
            inactivePokemon = activePokemon
            activePokemon = temp

        ending = ""
        if (activePokemon.hp <= 0):
            ending = " and they fainted, " + activePokemon.name + " loses!"
            battleDone = True
        else:
            ending = "."

        if (lastMove >= 0):
            drawMessage(screen, size, str(activePokemon.name) + " has been " + activePokemon.moves[lastMove].name + "ed" + str(ending))

        pygame.display.flip()