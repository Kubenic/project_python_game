import pygame, sys
from pygame import *

pygame.init()

tileswidthNumber = 50
tilesHeightNumber = 50
tilesHeightSize = 16
tilesWidthSize = 16

screenWidth = tilesWidthSize*tileswidthNumber
screenHeight = tilesHeightSize*tilesHeightNumber

fenetre = pygame.display.set_mode((screenWidth, screenHeight))
#Icone
image_icone = "DawnLike/Commissions/Icons.png"
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
titre_fenetre = "Super jeux !"
pygame.display.set_caption(titre_fenetre)


clock = pygame.time.Clock()
#BOUCLE PRINCIPALE
continuer = 1
while continuer:
	fenetre.fill((0,0,0))
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.update();
	continue