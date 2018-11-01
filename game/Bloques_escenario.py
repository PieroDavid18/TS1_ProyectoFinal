# Diseño: https://codepen.io/GeinerGV/pen/MPdMQN
from pygame import sprite, Surface, Color

TIPOS = {
	"SERPIENTE": {
		"ID": "1",
		"COLOR": "green",
		"SUBS": {
			"CABEZA": {"ID": 0},
			"CUERPO": {"ID": 1},
			"COLA": {"ID":2},
			"CONMANCHA": {"ID":3}
		}
	},
	"FONDO": {
		"ID": 0,
		"COLOR": "white"
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

# Función para obtener el color del bloque de acuerdo a tipo de bloque
def getTipoColor(tipoSelector):
		base = TIPOS
		color = "black"
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
			return Color(color)

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
	def __init__(self, dimX, dimY, tipo, level, serpiente):
		if (level == LEVELS["FACIL"]["ID"]):
			siz = 24
		elif (level==LEVELS["MEDIO"]):
			siz = 18
		elif (level==LEVELS["DIFICIL"]):
			siz = 12

class AreaBloque (Bloque):
	"""
	Conjunto de bloques organizados
	"""
	def __init__(self):
		self.


class Bloque (pygame.sprite.Sprite):
	'''
	# Hacer descripción
	'''
	def __init__(self, pos, tipo, wid, hei):
		self.tipo = tipo
		# self.color = getTipoColor(tipo)
		self.visible = False
		self.fragment = Surface.([wid, hei])
		self.inner = None


