from pygame import surface, draw

width,height = 1, 2
surf = surface.Surface([width, height])

class Person:
	lastKey = -1
	def __init__(self, name, age=30):
		self.name = name
		self.age = age
		self.surname = self.getSur1()
		self.key = Person.newLasKey()

	@staticmethod
	def newLasKey():
		Person.lastKey += 1
		return Person.lastKey
	
	def myfunc(self):
		print("Hello my name is " + self.name, isinstance(self.__class__, Person))
	
	def secfunc(self):
		print("Mi edad es " + str(self.age))
	def getSur1(self):
		sur = "Grandez"
		print(sur)
		return sur

class Geiner(Person):
	def __init__(self, *args):
		self.surname = self.getSur2()
		Person.__init__(self, *args)
	
	def myfunc2(self):
		print("Hello my name is " + self.name, issubclass(self.__class__, Geiner))
	def getSur2(self):
		sur = "Perez"
		print(sur)
		return sur
	def __repr__(self):
		return "Person(Geiner:repr)"
	def __str__(self):
		return "Person(Geiner:str)"

p1 = Geiner("Geiner", 12)
p1.myfunc2()
p1.secfunc()
print(p1)

x=5
def sumar(num):
	global x
	x += num

print(sumar(10))