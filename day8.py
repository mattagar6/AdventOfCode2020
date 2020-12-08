import sys

def go(vec):
	cur = 0
	val = 0
	vis = set()
	while cur < len(vec) and cur not in vis:
		vis.add(cur)
		if vec[cur][0] == "acc":
			val += vec[cur][1]
			cur += 1
		elif vec[cur][0] == "jmp":
			cur += vec[cur][1]
		else:
			cur += 1
	return val, cur >= len(vec)

def part1():
	print(go([(line.split()[0], int(line.split()[1])) for line in sys.stdin])[0])
	
def part2():
	vec = [[line.split()[0], int(line.split()[1])] for line in sys.stdin]
	n = len(vec)
	for i in range(n):
		if vec[i][0] == "nop":
			vec[i][0] = "jmp"
			val, ok = go(vec)
			if ok:
				print(val)
			vec[i][0] = "nop"
		elif vec[i][0] == "jmp":
			vec[i][0] = "nop"
			val, ok = go(vec)
			if ok:
				print(val)
			vec[i][0] = "jmp"
	
	
	
if __name__ == "__main__":
	# part1()
	part2()
