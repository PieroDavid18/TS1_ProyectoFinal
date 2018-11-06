import pygame
from screeninfo import get_monitors
from game.Escenarios import EscenarioCnt, simpleEscenario

FPS = 70
monitor = get_monitors()[0]
screen = (monitor.width, monitor.height)
del monitor

def main():
	pygame.init()
	ventana = pygame.display.set_mode(screen, (pygame.FULLSCREEN))
	pygame.display.set_caption("Snake Modo Usil")
	clock = pygame.time.Clock()
	manageEscenarios = EscenarioCnt(screen)
	manageEscenarios.draw(ventana)
	while True:
		clock.tick(FPS)
		manageEscenarios.ReRender(ventana)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				exit()
			""" if event.type == pygame.KEYDOWN:
				simple = simpleEscenario(manageEscenarios)
				simple.image = pygame.Surface([300, 300])
				simple.image.fill((255, 0, 0))
				simple.rect = simple.image.get_rect()
				manageEscenarios.draw(ventana) """
		# pygame.display.update((manageEscenarios.sprites()[0]))
		if manageEscenarios.actualizar:
			pygame.display.flip()
			manageEscenarios.actualizar = False
if __name__ == "__main__":
	main()
		