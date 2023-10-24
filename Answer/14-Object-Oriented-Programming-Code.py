class Account:
	"""
	>>> a = Account('John')
	>>> a.deposit(100)
	100
	>>> a.withdraw(90)
	10
	>>> a.withdraw(90)
	'chi xin wang xiang'
	>>> a.balance
	10
	"""
	deposit = 666
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
	#	self.deposit = 999

	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return 'chi xin wang xiang'
		self.balance = self.balance - amount
		return self.balance


