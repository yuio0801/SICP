def rfactorial(n):
	if n == 0:
		return 1
	else:
		return n * rfactorial(n-1)

def ifactorial(n):
	total = 1
	while n > 0:
		total *= n
		n -= 1
	return total

