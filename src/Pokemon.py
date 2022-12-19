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


class Pokemon: # TODO add some randomness
    def __init__(self, frontImg, backImg):
        self.hp = 100
        self.moves = { 
            "Punch": 10, 
            "Scratch": 5, 
            "Kick": 7.5 
        }

        self.renderable = PokemonRenderable(frontImg, backImg)

    def getAttacked(self, moves, key):
        self.hp -= moves[key]