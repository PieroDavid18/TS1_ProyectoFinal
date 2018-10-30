# Diseño: https://codepen.io/anon/pen/LgomZd
import pygame.sprite

TIPOS = {
	"SERPIENTE": {
		"CABEZA": 2,
		"CUERPO": 1,
		"COLA": 3,
		"CONMANCHA": 4
	},
	"FONDO": 0
}

class Bloque_escenario (pygame.sprite.Sprite):
	'''
	# Hacer descripción
	'''
	size = 10
	def __init__(self, tipo):


