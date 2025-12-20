import pygame
from pygame.locals import *
import sys
import time
import random

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("particle sim")
clock = pygame.time.Clock()

TAILLE_CELL = 5

taille_texte = pygame.font.SysFont(None,30)
largeur_ecran , hauteur_ecran = screen.get_size()
largeur_bouton = 50
hauteur_bouton = 50
xbouton = (largeur_ecran-largeur_bouton)//12
ybouton = (hauteur_ecran-hauteur_bouton)//2

text_box = None
bouton_sable = pygame.Rect(xbouton,ybouton,largeur_bouton,hauteur_bouton)
bouton_block = pygame.Rect(xbouton,ybouton+100,largeur_bouton,hauteur_bouton)

min_y = 40
max_y = 140
max_x = 140
min_x = 40

BLEU = (70, 130, 180)
NOIR = (20, 20, 20)
GRIS = (40, 40, 40)
GRIS_CLAIR = (150, 150, 150)
Jaune = (212, 183, 106)

grille = {}

class particule():
    def __init__(self,x,y,couleur = None):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.taille = 4

    def Dessiner(self,surface):
        px = self.x * self.taille
        py = self.y * self.taille
        pygame.draw.rect(surface, self.couleur, (px, py, self.taille, self.taille))

class sable(particule):
    def __init__(self, x, y):
        super().__init__(x, y, couleur = Jaune)
        self.grav = 1

    def ChekVoisins(self,grille):

        bas = (self.x, self.y + self.grav)
        diag1 = (self.x + 1,self.y + 1)
        diag2 = (self.x - 1,self.y + 1)

        if min_y<self.y+self.grav<max_y and not grille[bas] in grille :
            del grille[(self.x,self.y)]
            self.y+=self.grav
            grille[(self.x,self.y)] = self

class block(particule):
    #cet objet ne bouge jamais appart si il est enlever manuellement 
    def __init__(self, x, y, couleur=None):
        super().__init__(x, y, couleur=NOIR)

    def ChekVoisins(self,grille):
        pass 

def afficher_grille(surface, grille):
    zone_jeu = pygame.Rect(min_x * TAILLE_CELL, min_y * TAILLE_CELL, 
                           (max_x - min_x) * TAILLE_CELL, (max_y - min_y) * TAILLE_CELL)
    pygame.draw.rect(surface, (30, 30, 30), zone_jeu)  # Fond gris foncé

    for (x, y), ent in grille.items():
        couleur = ent.couleur
        rect = pygame.Rect(x * TAILLE_CELL, y * TAILLE_CELL, TAILLE_CELL, TAILLE_CELL)
        pygame.draw.rect(surface, couleur, rect)

def afficher_texte(texte, x, y,largeur,hauteur,couleur,taille):
    if isinstance(texte,list):
        texte = ''.join(texte)
        
    rendu = taille.render(texte, True, couleur)
    screen.blit(rendu, ((x+largeur//2)-100, y+hauteur//2))

object = None 

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

        if event.type == MOUSEBUTTONDOWN :
            if bouton_sable.collidepoint(pygame.mouse.get_pos()):
                object = "sable"
                text_box = "Vous avez selectioner le sable"

            if bouton_block.collidepoint(pygame.mouse.get_pos()):
                object = "block"
                text_box = "Vous avez selectionner les blocks"

        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            x, y = event.pos
            case_x = x // TAILLE_CELL
            case_y = y // TAILLE_CELL

            if min_x<case_x<max_x and min_y<case_y<max_y :

                if object == "sable":
                    grille[case_x,case_y] = sable(case_x,case_y)

                elif object == "block":
                    grille[case_x,case_y] = block(case_x,case_y)


    grille_items = list(grille.items())
    
    grille_items.sort(key=lambda item: item[0][1], reverse=True)
    
    for pos, ent in grille_items:
        if isinstance(ent, sable):
            ent.ChekVoisins(grille)
    


    screen.fill(GRIS_CLAIR)
    afficher_grille(screen,grille)
    pygame.draw.rect(screen,Jaune,bouton_sable)
    pygame.draw.rect(screen,NOIR,bouton_block)
    afficher_texte(text_box,xbouton,20,largeur_bouton+150,hauteur_bouton,NOIR,taille_texte)
    pygame.display.flip()

    clock.tick(60)