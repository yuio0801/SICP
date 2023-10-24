class Dog:

	def __init__(self):
		self.__repr__ = lambda: 'teddy'
		self.__str__=  lambda: 'a teddy'

	def __repr__(self):
		return 'Dog()'

	def __str__(self):
		return 'this is a dog'

def repr(x):
	return type(x).__repr__(x)

def str(x):
	t = type(x)
	if hasattr(t, '__str__'):
		return t.__str__(x)
	else:
		return repr(x)
	
teddy = Dog()
print(teddy)
print(repr(teddy))
print(str(teddy))
print(teddy.__repr__())
print(teddy.__str__())
	

