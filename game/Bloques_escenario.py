# Diseño: https://codepen.io/GeinerGV/pen/MPdMQN
import pygame.sprite

TIPOS = {
	"SERPIENTE": {
		"ID": "1",
		"COLOR": "RGB(118,238,0)",
		"SUBS": {
			"CABEZA": {"ID": 0},
			"CUERPO": {"ID": 1},
			"COLA": {"ID":2},
			"CONMANCHA": {"ID":3}
		}
	},
	"FONDO": {
		"ID": 0,
		"COLOR": "RGB(255, 255,255)"
	}
}
LEVELS = {
	"FACIL": {
		"ID": 1,
		"SIZ": 24
	},
	"MEDIO": {
		"ID": 2,
		"SIZ": 18
	},
	"DIFICIL": {
		"ID": 3,
		"SIZ": 12
	}
}
'''
class Bloque_facil (Bloque):
	siz = 24
	def __init__(self):
		super(self)
'''

class Tablero (pygame.sprite.Sprite):
	'''
	El área de juego
	'''
	def __init__(self, dimX, dimY, tipo, level):
		if (level == LEVELS["FACIL"]["ID"]):
			siz = 24
		elif (level==LEVELS["MEDIO"]):
			siz = 18
		elif (level==LEVELS["DIFICIL"]):
			siz = 12

def getTipoColor(tipoSelector):
		base = TIPOS
		color = "RGB(0, 0, 0)"
		arrTipo = tipoSelector.split(".")
		continuar = True
		for idx in arrTipo:
			if not continuar:
				break
			for tipo in base:
				if tipo.ID == idx:
					try:
						color = tipo.COLOR
					except:
						print(tipo.ID, "sin color")
					try:
						base = tipo.SUBS
					except:
						continuar = False
					break
			return color

class Bloque (pygame.sprite.Sprite):
	'''
	# Hacer descripción
	'''
	siz = 0
	def __init__(self, posX, posY, tipo):
		self.tipo = tipo
		self.len = len
		self.color = getTipoColor(tipo)
		

