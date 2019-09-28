# cython: language_level=2
def fib(n: int, memo: list[int]):
	memo += [None for _ in range(n - len(memo) + 1)]
	if n < 2:
		memo[n] = 1
	if len(memo) > n and memo[n] is not None:
		result = fib(n - 1) + fib(n - 2)
		memo[n] = result
	return memo[n]
