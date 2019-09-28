import pyximport; pyximport.install()
import cython_modules
from timeit import timeit

def fib(n, memo):
	memo += [None for _ in range(n - len(memo) + 1)]
	if n < 2:
		memo[n] = 1
	if len(memo) > n and memo[n] is not None:
		result = fib(n - 1) + fib(n - 2)
		memo[n] = result
	return memo[n]

def parser(s):
	ret = ""
	for c in s:
		try:
			ret += str(int(c))
		except ValueError:
			ret += ""
	return int(ret)


number = 10
for i in range(6, 31, 2):
	py_time = timeit(f"fib(i, [])", number=number, globals=globals())
	cy_time = timeit(f"cython_modules.fib(i, [])", number=number, globals=globals())
	print(f"fib({i}) / executed {number} times / cython is x{py_time / cy_time:.3f} faster")

s = "11oe3f5n4oyi674n7e45o746765i8568n5es"
py_time = timeit(f"parser(s)", number=1, globals=globals())
cy_time = timeit(f"cython_modules.parser(s)", number=1, globals=globals())
print(f"parser({s}) / cython is x{py_time / cy_time:.3f} faster")
