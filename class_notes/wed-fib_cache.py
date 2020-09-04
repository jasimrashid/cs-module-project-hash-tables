# 0 1 1 2 3 5 8 13 21 34 55

# Memorization, "caching"
# Top-Down Dynamic Programming

cache = {}

def fib(n):
	if n <= 1:
		return n

	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)

		# return fib(n-1) + fib(n-2) #1 recursion method	
	return cache[n]

for i in range(5):
	print(f"{i}: {fib(i)}")
