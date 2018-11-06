import time, sys, pygame
from Bloques import Tablero

FPS = 40


resolution = (25*20, 25*20)

def main():
	pygame.init()
	ventana = pygame.display.set_mode((1300, 700))
	pygame.display.set_caption("Prueba")
	ventana.fill((210,210,210))
	clock = pygame.time.Clock()
	tab = Tablero(0, (1300, 700))
	tab.draw(ventana)
	new = True
	while True:
		clock.tick(FPS)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
		if new:
			new = False
			pygame.display.flip()

main()

