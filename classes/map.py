import pytmx, pygame
class Map():

	def __init__(self, url):
		self.url = url
		self.tmxdata = pytmx.TiledMap(url)
		self.tileWIdth = 16
		self.tileHeight = 16
		self.tiles=[]
		self.loadedImages =[]
		self.loadTiles();
		#print(self.loadedImages)
		#print(self.tmxdata.layers)

	def loadTiles(self):
		for layer in self.tmxdata.layers:
			if(layer.name == "Tiles"):
				for tile in layer.tiles():
					#print(tile[2])

					#tile[2][0] = pygame.image.load(tile[2][0])
					loaded = (tile[2][0], pygame.image.load(tile[2][0]))
					self.loadedImages.append(loaded)
					self.tiles.append(tile)
					#print(self.tiles)

	def displayTiles(self, screen):
		for layer in self.tmxdata.layers:

			if (layer.name == "Tiles"):
				for x, y, image in layer.tiles():
					
					imageToUse = pygame.image.load(image[0])
					imageToUse.set_clip(image[1][0], image[1][1], image[1][2], image[1][3])
					finalImage = imageToUse.subsurface(imageToUse.get_clip())
					screen.blit(finalImage,(x*self.tileWIdth,y*self.tileHeight,x*self.tileWIdth,x*self.tileHeight))


