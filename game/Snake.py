class Snake:
	"""
	Esta es la serpiente de nuestro juego
	"""
	default_color = "verde"
	def __init__(self, posX, posY, longitud, direccion, vidas):
		self.x = posX
		self.y = posY
		self.longitud = longitud
		self.direccion = direccion
		self.vidas = vidas
		self.alimentos = 0

	def comerAlimento(self):
		self.alimentos += 1
	
	def moverX(self, newPosX):
		self.x = newPosX
	
	def moverY(self, newPosY):
		self.y = newPosY

	def conVida(self):
		return True if self.vidas > 0 else False

	def perderVida(self):
		if self.conVida():
			self.vidas -= 1

	
