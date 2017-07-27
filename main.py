import pygame, sys, pytmx
from pprint import pprint
from pygame import *
from pygame import display
from classes.player import Player
from classes.map import Map
from pytmx.util_pygame import load_pygame


#tmxdata = load_pygame("DawnLike/Examples/Mine.tmx")
#image = tmxdata.get_title_image(16,16,Tiles)

#tmxdata = pytmx.TiledMap("DawnLike/Examples/Mine.tmx")
#print(tmxdata.properties)
#print(tmxdata.map)
#for layer in tmxdata.layers:
#	for x, y, image in layer.tiles():
#		print(x)
#		print(y)
#		print(image)
#		for url, dimension, flags in image

#for layer in tmxdata.visible_layers:
#	print(layer)
#	if(layer.get('name') == "Tiles"):
#		print(layer)
#tiled_map = load_pygame("DawnLike/Examples/Mine.tmx", invert_y=True)

#with open('map.json') as data_file:    
#	data = json.load(data_file)

#print(len(data["map"][0]))
#props = tmxdata.get_layer_by_name("Obstacles").properties
#print(props)

#import xml.etree.ElementTree
#e = xml.etree.ElementTree.parse("DawnLike/Examples/Mine.tmx").getroot()
#for atype in e.findall('objectgroup'):
#    print(atype.get('name'))
#    if(atype.get('name') == "Obstacles"):
#    	for btype in atype.findall('object'):
#    		print(btype.get('id'))
joueur = Player((10,10))
map = Map("DawnLike/Examples/Mine.tmx")
pygame.init()

tileswidthNumber = 19
tilesHeightNumber = 15
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
map.displayTiles(fenetre)
#BOUCLE PRINCIPALE
continuer = 1
while continuer:
	#fenetre.fill((0,0,0))
	clock.tick(60)
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	joueur.handle_event(event)
	fenetre.blit(joueur.image, joueur.rect)
	pygame.display.update();
	continue