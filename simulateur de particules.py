import pygame
from pygame.locals import *
import sys
import time
import random

TAILLE_CELL = 2
N = 150
BLEU = (70, 130, 180)
NOIR = (20, 20, 20)
GRIS = (40, 40, 40)
Jaune = (212, 183, 106)

class particule():
    def __init__(self,x,y, grav = 1):
        self.x = x
        self.y = y
        self.type = 'sable'
        self.taille = 5
        self.vie = False
        self.next_vie = False
        self.grav = grav
        self.couleur = Jaune if self.vie else NOIR

    def Update(self):
        self.vie = self.next_vie
        self.couleur = Jaune if self.vie else NOIR

    def reveil(self):
        self.next_vie= True

    def mort(self):
        self.next_vie = False

    def Dessiner(self,surface):
        px = self.x * self.taille
        py = self.y * self.taille
        pygame.draw.rect(surface, self.couleur, (px, py, self.taille, self.taille))

    def CheckVoisins(self, grille):

        bas = (self.x, self.y + self.grav)

        if bas not in grille :
            self.next_vie = True

        elif bas in grille and not grille[bas].vie :
            self.next_vie = False
            grille[bas].next_vie = True

        else :    
            diag1 = (self.x + 1,self.y + 1)
            diag2 = (self.x - 1,self.y + 1)

            if diag1 in grille and not grille[diag1].vie :
                grille[diag1].next_vie = True
                self.next_vie = False

            elif diag2 in grille and not grille[diag2].vie :
                grille[diag2].next_vie = True
                self.next_vie = False

            else :
                self.next_vie = True

def creer_grille(N):
    grille = {}
    for y in range(N):
        for x in range(N):
            grille[(x,y)] = particule(x,y)
        
    return grille


def afficher_grille(screen, dico):
    for cell in dico.values():
        rect = pygame.Rect(cell.x * TAILLE_CELL, cell.y * TAILLE_CELL, TAILLE_CELL, TAILLE_CELL)
        pygame.draw.rect(screen, cell.couleur, rect)


pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("sable simulator")
clock = pygame.time.Clock()
grille = creer_grille(N)

loop = True
while loop :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()

    mouse_state = pygame.mouse.get_pressed()
    if mouse_state[0]:
        x_pixel, y_pixel = event.pos
        case_x = x_pixel // TAILLE_CELL
        case_y = y_pixel // TAILLE_CELL

        if (case_x, case_y) in grille:
            grille[(case_x, case_y)].reveil()


    for y in range(N):
        for x in range(N):
            if grille[(x,y)].vie :
                grille[(x,y)].CheckVoisins(grille)

    for y in range(N):
        for x in range(N):
            grille[(x,y)].Update()


    screen.fill(GRIS)
    afficher_grille(screen, grille)
    pygame.display.flip()

    clock.tick(90)
    