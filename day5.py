import sys

def go(s):
	lo, hi = 0, 128
	for i in range(7):
		mid = (lo+hi)/2
		if s[i] == "F":
			hi = mid
		else:
			lo = mid
	row = lo
	lo, hi = 0, 8
	for i in range(3):
		mid = (lo+hi)/2
		if s[i+7] == "L":
			hi = mid
		else:
			lo = mid
	col = lo
	return row * 8 + col

def part1():
	ans = 0
	for line in sys.stdin:
		ans = max(ans, go(line))
	print(ans)

def part2():
	seats = {go(line) for line in sys.stdin}
	for x in range(1<<10):
		if x-1 in seats and x+1 in seats and x not in seats:
			print(x)

if __name__ == "__main__":
	# part1()
	part2()
