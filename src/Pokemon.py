import pygame
from pygame.math import Vector2

class PokemonRenderable:
    def __init__(self, frontImg, backImg):
        self.front = pygame.image.load(frontImg)
        self.back = pygame.image.load(backImg)

        self.frontRect = self.front.get_rect()
        self.backRect = self.back.get_rect()

        self.facingForward = True

        self.position = Vector2(0, 0)

    def draw(self, screen):
        self.frontRect.center = self.position
        self.backRect.center = self.position

        if (self.facingForward):
            screen.blit(self.front, self.frontRect)
        else:
            screen.blit(self.back, self.backRect)
        
    def flip(self):
        if (self.facingForward):
            self.facingForward = False
        else:
            self.facingForward = True

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.selected = False

class Pokemon: # TODO add some randomness
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.maxHp = 100

        self.moves = [ 
            Move("Punch", 10), 
            Move("Scratch", 5), 
            Move("Kick", 7.5)
        ]

        self.renderable = PokemonRenderable("assets/images/" + name + "_Front.png", "assets/images/" + name + "_Back.png")

    def getAttacked(self, move):
        self.hp -= move.damage
