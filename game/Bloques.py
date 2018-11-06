from pygame import sprite, surface, Color
from Claves import Clave

from pygame import time

class Escenarios(sprite.Group):
	def __init__(self, screen, escenario):
		sprite.Group.__init__(self)
		self.espacios = {"tablero": screen}
		self.escenario = escenario

	def NewTablero(self, fondo, estructura):
		self.tablero_cnt = AreaTablero(self.espacios["tablero"], fondo)
		# areaTablero.rect.move_ip(0, 0)
class EscenarioCnt(sprite.GroupSingle):
	def __init__(self):
		sprite.GroupSingle.__init__(self)

class EscenarioView(sprite.Sprite):
	colors = ["green"]
	def __init__(self, screen, timer):
		self.image = surface.Surface(screen)

class AreaTablero(sprite.Sprite):
	def __init__(self, size, bgcolor):
		self.image = surface.Surface(size)
		self.image.fill(Color(bgcolor))
		self.rect = self.image.get_rect()

	# def 

class TableroCnt(sprite.GroupSingle):
	def __init__(self):
		pass
class Tablero(sprite.Sprite):
	def __init__(self, color):
		self

class ItemsTablero(sprite.Group):
	def __init__(self, rangoCelda, maxSize, colors = ("#b6c25a", "#afbc54"), estructura = None):
		sprite.Group.__init__(self)
		self.colors = (colors[0], colors[1]) # determinar 2 colores
		self.rangeSize = (rangoCelda[0], rangoCelda[1]) # determinar rango del tamaño de la celda
		self.sizeCelda = self.rangeSize[0]
		self.templates = []
		for color in self.colors:
			temp = surface.Surface([self.sizeCelda, self.sizeCelda])
			temp.fill(Color(color))
			self.templates.append(temp)
		self.actualizar = {"templates": [False, False]}
		self.dimesion = (int(maxSize[0]/self.sizeCelda), int(maxSize[1]/self.sizeCelda))
		if isinstance(estructura, int):
			if estructura == 1:
				from Estructuras import Estructura1 as estructura
				for fila in range(self.dimesion[0]):
					for col in range(self.dimesion[1]):
						if estructura[fila][col] == 1:
							self.add(Celda(self.templates[(fila+col)%2], pos=(fila, col)))
			else:
				estructura = None
		if estructura == None:
			for fila in range(self.dimesion[0]):
				for col in range(self.dimesion[1]):
					self.add(Celda(self.templates[(fila+col)%2], pos=(fila, col)))

class Celda(sprite.Sprite):
	def __init__(self, base, **kargs):
		sprite.Sprite.__init__(self)
		if isinstance(base, surface.Surface):
			self.image = base
		elif isinstance(base, (list, tuple)):
			self.image = surface.Surface([base[0], base[1]])

		self.rect = self.image.get_rect()
		if "pos" in kargs:
			base = self.image.get_size()
			self.rect.move_ip(base[0] * kargs["pos"][0], base[1] * kargs["pos"][1])
	def getPos(self):
		pixPos = self.image.get_offset()
		size = self.image.get_size()
		return (pixPos[0]/size[0], pixPos[1]/size[1])
	def update(self):
		PosParOImpar = sum(self.getPos())%2
		actualizar = self.groups()[0].actualizar["templates"][PosParOImpar]
		if actualizar:
			pos = self.image.get_offset()
			self.image = self.groups()[0].templates[PosParOImpar]
			self.rect = self.image.get_rect()
			if pos != self.image.get_offset():
				self.rect.move(*pos)

class BloqueCuerpoSerpiente(sprite.Group):
	colors = ["blue", "yellow", "orange"]
	def __init__(self, tablero, lenInit):
		sprite.Group.__init__(self)
		self.tablero = tablero
		self.template = surface.Surface([self.tablero.sizeCelda, self.tablero.sizeCelda])

	def getTemplates(self):
		pass

class PiezaSerpiente(sprite.Sprite):
	def __init__(self, direction, puesto, lenPiezas, **kargs):
		sprite.Sprite.__init__(self)
		self.direction = direction
		self.puesto = puesto
		# self.image = base
		self.rect = self.image.get_rect()
		if "pos" in kargs:
			base = self.image.get_size()
			self.rect.move_ip(base[0] * kargs["pos"][0], base[1] * kargs["pos"][1])

class Bloque(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)