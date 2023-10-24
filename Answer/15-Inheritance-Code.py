class Account:

	interest = 0.02

	def __init__(self, account_holder):
		self.holder = acount_holder
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if self.balance < amount:
			return 'chi xin wang xiang'
		self.balance -= amount
		return self.balance

class CheckingAccount(Account):
	interest = 0.01
	withdraw_fee = 1
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)
#		return super().withdraw(amount+self.withdraw_fee)
