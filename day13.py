import sys
	
def part1():
	T = float("inf")
	idx = -1
	t = int(input())
	times = list(map(int, filter(lambda x: x != "x", [line.split(",") for line in sys.stdin][0])))
	
	for x in times:
		first = x * ((t + x - 1) // x)
		if first - t < T - t:
			T = first
			idx = x

	print(idx * (T - t))

def part2():

	def pw(a, n, mod):
		r = 1
		while n > 0:
			if n % 2 == 1:
				r = r * a % mod
			a = a * a % mod
			n >>= 1
		
		return r
	
	_ = input()
	times = [line.split(",") for line in sys.stdin][0]
	n = len(times)
	for i in range(n):
		if times[i] != "x":
			times[i] = int(times[i])
	
	prod = 1
	for x in times:
		if x != "x":
			prod *= x
			
	X = [1] * n
	for i, x in enumerate(times):
		if x != "x":
			X[i] = prod / x
	
	ans = 0
	for i, x in enumerate(times):
		if x != "x":
			want = ((-i) % times[i] + times[i]) % times[i]
			ans += want * X[i] * pw(X[i], x-2, x)
	
	ans %= prod
	print(ans)

if __name__ == "__main__":
	# part1()
	part2()
