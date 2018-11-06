class Clave:
	lastKey = -1
	def __init__(self):
		self.clave = self.newKey()

	def __repr__(self):
		return self.clave

	def __str__(self):
		return "Clave(%s)" % self.clave

	@staticmethod
	def newKey():
		Clave.lastKey += 1
		return format(Clave.lastKey, 'x')