if ibonacci

# Fibonacci numbers module

#n = int(input('Please enter an number:'))

def fib(n):		# write fibonacci series up to nu
	a,b = 0,1
	while a < n:
			print(a, end=' ')
			a,b = b, a+b
	print()