import sys

def part1():
	cur = set()
	ans = 0
	for line in sys.stdin:
		if line == "\n":
			ans += len(cur)
			cur = set()
		else:
			cur |= set(line[:-1])
	print(ans)

def part2():
	cur = set()
	prv = "\n"
	ans = 0
	for line in sys.stdin:
		if line == "\n":
			ans += len(cur)
			cur = set()
		else:
			cur = set(line[:-1]) if prv == "\n" else cur & set(line[:-1])
		prv = line
	print(ans)
	
if __name__ == "__main__":
	# part1()
	part2()
