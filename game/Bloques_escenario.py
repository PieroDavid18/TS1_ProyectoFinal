# Diseño: https://codepen.io/GeinerGV/pen/MPdMQN
from pygame import sprite, surface, Color, draw
from Variables import TIPOS, LEVELS, tipos_anonimos

# Función para obtener el color del bloque de acuerdo a tipo de bloque
def getTipoColor(tipoSelector):
		color = TIPOS["ANONIMO"]["COLOR"]
		arrTipo = tipoSelector.split(".")
		base = tipos_anonimos if arrTipo[0] == 0 and len(arrTipo)>1 else TIPOS

		for i in range(len(arrTipo)):
			for idx in base:
				tipo = base[idx]
				if tipo["ID"] == arrTipo[i]:
					if "COLOR" in tipo:
						color = tipo["COLOR"]
					break
			if i < len(arrTipo)-1:
				if "SUBS" in base:
					base = base["SUBS"] if arrTipo[0] == 0 else base["SUBS"].items()
				else:
					return Color(color)

class AreaBloque (sprite.Group):
	"""
	Conjunto de bloques organizados
	"""
	def __init__(self, *bloques, config = dict()):
		#Bloque.__init__(self, )
		self.config = config
		self.config.setdefault("ordenado", True)
		self.config.setdefault("movimiento", "bloque")
		sprite.Group.__init__(self, *bloques)
		if len(bloques):
			claves = map(lambda bloque: bloque.key, bloques)
			self.bloques = list(claves) if self.config["ordenado"] else set(claves)
		else:
			self.bloques = list() if self.config["ordenado"] else set()
		if "bloque" in config and issubclass(config["bloque"], Bloque):
			self.bloque = CntBloque.fromBloque(config["bloque"])
		else:
			self.bloque = CntBloque(config=dict(w=config["w"], h=config["h"]))
		Bloque.lista_bloques[self.bloque.key] = self

class Bloque(sprite.Sprite):
	""" Bloque base para el tablero """
	lista_bloques = dict()
	def __init__(self, config=dict(), base=None):
		sprite.Sprite.__init__(self)
		self.key = Clave()
		self.isCnt = False
		
		# Almacenar como bloque
		if not issubclass(self.__class__, CntBloque): Bloque.lista_bloques[self.key] = self
		
		# Establecer el bloque padre
		if isinstance(base, (Bloque, Clave)):
			self.base = base.key if isinstance(base, Bloque) else base
		else:
			self.base = None
		
		# crear elementos
		if self.estaBasado():
			config.setdefault("w", self.width())
			config.setdefault("h", self.heigth())
		if config["copiar"]:
			self.image = self.lista_bloques[self.base].image.copy()
		else:
			self.image = surface.Surface([config["w"], config["h"]])
		self.rect = self.image.get_rect()
	
	def estaBasado(self):
		if self.base == None:
			return False
		return True

	def width(self):
		if self.estaBasado():
			return self.lista_bloques[self.key].width()
		return self.image.get_width()

	def heigth(self):
		if self.estaBasado():
			return self.lista_bloques[self.key].heigth()
		return self.image.get_height()

class CntBloque(Bloque):
	def __init__(self, **args):
		Bloque.__init__(self, **args)
		self.isCnt = True
	@staticmethod
	def fromBloque(bloque):
		bloque.isCnt = True
		return bloque

class Clave:
	lastKey = -1
	def __init__(self):
		self.clave = self.newKey()

	def __repr__(self):
		return self.clave

	def __str__(self):
		return self.clave

	@staticmethod
	def newKey():
		Clave.lastKey += 1
		return format(Clave.lastKey, 'x')

class AreaBloque (sprite.Group):
	"""
	Conjunto de bloques organizados
	"""
	def __init__(self, *bloques, config = dict()):
		#Bloque.__init__(self, )
		sprite.Group.__init__(self, *bloques)
		self.config = config
		self.config.setdefault("ordenado", True)
		self.config.setdefault("movimiento", "bloque")

		# temp
		if len(bloques):
			claves = map(lambda bloque: bloque.key, bloques)
			self.bloques = list(claves) if self.config["ordenado"] else set(claves)
		else:
			self.bloques = list() if self.config["ordenado"] else set()
		# end temp

		if "bloque" in config and issubclass(config["bloque"], Bloque):
			config["bloque"].toAreaBloque()
			self.bloque = config["bloque"]
		else:
			self.bloque = Bloque({"w": self.config["w"], "h": self.config["h"], "isContenedor":True})
		Bloque.lista_bloques[self.bloque.key] = self

class Bloque(sprite.Sprite):
	lista_bloques = dict()
	def __init__(self, config = dict(), base=None):
		sprite.Sprite.__init__(self)
		self.key = Clave()
		config.setdefault("isContenedor", False)
		self.isContenedor = config["isContenedor"]
		# self.isPainted = False
		if not self.isContenedor: Bloque.lista_bloques[self.key] = self
		
		if isinstance(base, (Bloque, Clave)):
			self.base = base.key if isinstance(base, Bloque) else base
			self.image = self.lista_bloques[self.base].image.copy()
		elif isinstance(base, surface.Surface):
			self.image = base
			self.base = None
		else:
			self.image = surface.Surface((config["w"], config["h"]))
			self.base = None
		if "color" in config:
			color = Color(config["color"]) if isinstance(config["color"], str) else config["color"]
			self.image.fill(color)
		self.rect = self.image.get_rect()

	@classmethod
	def fromOther(cls, bloque):
		return cls(base=bloque)
	
	def toAreaBloque(self):
		self.isContenedor = True

class TableroPrueba(AreaBloque):
	def __init__(self, filas, columnas, wCelda, hCelda):
		AreaBloque.__init__(self, config={"w": columnas*wCelda, "h": filas*hCelda})
		colors = ["blue", "orange"]
		for fila in range(filas):
			for col in range(columnas):
				color = colors[(fila+col)%2]
				tmpBloque = Bloque({"w": wCelda, "h": hCelda, "color": color})
				tmpBloque.rect.move_ip(col*wCelda, fila*hCelda)
				self.add(tmpBloque)