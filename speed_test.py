import pyximport; pyximport.install()
from cython_modules import fib as cy_fib
from timeit import timeit

def fib(n):
	if n < 2:
		return 1
	return fib(n - 1) + fib(n - 2)


number = 10
for i in range(6, 31, 2):
	py_time = timeit(f"fib(i)", number=number, globals=globals())
	cy_time = timeit(f"cy_fib(i)", number=number, globals=globals())
	print(f"fib({i}) / executed {number} times / cython is x{py_time / cy_time:.3f} faster")
