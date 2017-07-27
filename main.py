import pygame, sys, json
from pprint import pprint
from pygame import *
from classes.player import Player
from classes.monster import Monster

with open('map.json') as data_file:
    data = json.load(data_file)

print(len(data["map"][0]))

joueur = Player((300, 200))
monster = Monster((400, 300))
pygame.init()

tileswidthNumber = 50
tilesHeightNumber = 50
tilesHeightSize = 16
tilesWidthSize = 16

screenWidth = tilesWidthSize * tileswidthNumber
screenHeight = tilesHeightSize * tilesHeightNumber

fenetre = pygame.display.set_mode((screenWidth, screenHeight))

# Icone
image_icone = "DawnLike/Commissions/Icons.png"
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

# Titre
titre_fenetre = "Super jeux !"
pygame.display.set_caption(titre_fenetre)

clock = pygame.time.Clock()

# BOUCLE PRINCIPALE
continuer = 1
while continuer:
    fenetre.fill((0, 0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    fenetre.blit(pygame.transform.scale(monster.image, (30, 30)), monster.rect)

    joueur.handle_event(event)
    fenetre.blit(pygame.transform.scale(joueur.image, (30, 30)), joueur.rect)
    fenetre.blit(pygame.transform.scale(joueur.arm_img, (30, 30)), joueur.arm_rect)


    pygame.display.update();
    continue
