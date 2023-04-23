import pygame
import pygame.gfxdraw
from particule import *
from random import randint

pygame.init()

# définition de la taille de la fenetre
LARGEUR = int(input("Entrez la largeur de votre écran (en pixel) : "))
HAUTEUR = int(input("Entrez la hauteur de votre écran (en pixel) : "))

nb_particules = int(input("Combien de particules voulez-vous afficher ? : "))

# création de la fenetre
fenetre = pygame.display.set_mode((HAUTEUR, LARGEUR), pygame.FULLSCREEN)

zone_texte = pygame.font.SysFont(None, 24)
texte1 = zone_texte.render("Click-gauche : Attraction (peut causer un crash)", True, (155, 155, 155))
texte2 = zone_texte.render("Click-droit  : Changement de direction", True, (155, 155, 155))

# on créé une liste de particules
lst_particules = []

for i in range(nb_particules):
    p = Particule(x=randint(0, LARGEUR),
                  y=randint(0, HAUTEUR),
                  taille=randint(4, 10),
                  xvitesse=randint(-2, 2),
                  yvitesse=randint(-2, 2),
                  masse=1,
                  couleur=(255, 255, 255))

    lst_particules.append(p)

# définition du centre de gravité
centre = Particule(pygame.mouse.get_pos()[0],
                   pygame.mouse.get_pos()[1],
                   10,
                   0,
                   0,
                   1,
                   (255, 0, 0))

# boucle infinie qui fait tourner le programme
running = True
while running:

    # vérifie si la fenêtre est fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fond noir + texte
    fenetre.fill((0, 0, 0))
    fenetre.blit(texte1, (20, 20))
    fenetre.blit(texte2, (20, 40))

    # boucle déterminant la position des particules et leur affichage
    for i in range(len(lst_particules)):
        centre.x = pygame.mouse.get_pos()[0]
        centre.y = pygame.mouse.get_pos()[1]
        attraction = pygame.mouse.get_pressed()
        # séparation entre une particule choisie et le reste de la liste
        particule = lst_particules[i]
        nv_lst = [p for p in lst_particules if p != particule]

        particule.calculeAcceleration(nv_lst, centre, attraction, LARGEUR, HAUTEUR)
        particule.mettreMouvement()
        particule.changementCouleur(nv_lst)

        pygame.gfxdraw.filled_circle(fenetre,
                                     int(particule.x),
                                     int(particule.y),
                                     particule.taille,
                                     particule.couleur)

    # met à jour le display (écran)
    pygame.display.flip()

pygame.quit()
