import sys
input = sys.stdin.readline

def part1():
	ivs = []
	for line in sys.stdin:
		if line == "\n":
			break
		else:
			line = line.strip()
			[_, s] = line.split(":")
			s = s.strip()
			l = s.split(" or ")
			for x in l:
				[L, R] = map(int, x.split("-"))
				ivs.append((L, R))

	prv = ""
	ans = 0
	for line in sys.stdin:
		line = line.strip()
		if prv and prv[0] == "n":
			vec = map(int, line.split(","))
			for x in vec:
				ok = False
				for L, R in ivs:
					if L <= x <= R:
						ok = True
				if not ok:
					ans += x
		else:
			prv = line

	print(ans)

def part2():
	ivs = []
	for line in sys.stdin:
		if line == "\n":
			break
		else:
			line = line.strip()
			[_, s] = line.split(":")
			s = s.strip()
			l = s.split(" or ")
			cur = []
			for x in l:
				[L, R] = map(int, x.split("-"))
				cur.append((L, R))
			ivs.append(cur)

	n = len(ivs)
	mask = [(1<<n)-1] * n
	prv = ""
	me = []
	ans = 0
	for line in sys.stdin:
		line = line.strip()
		if prv and prv[0] == "y":
			me = map(int, line.split(","))
			prv = line
		elif prv and prv[0] == "n":
			vec = map(int, line.split(","))
			im_good = True
			for i, x in enumerate(vec):
				ok = False
				for a, b in ivs:
					if a[0] <= x <= a[1] or b[0] <= x <= b[1]:
						ok = True
				if not ok:
					im_good = False
					
			if im_good:
				for i, x in enumerate(vec):
					can = (1<<n)-1
					for j in range(n):
						ok = False
						for k in range(2):
							if ivs[j][k][0] <= x <= ivs[j][k][1]:
								ok = True
						if not ok:
							can ^= 1<<j
					mask[i] &= can
		else:
			prv = line

	for rep in range(n):
		for i in range(n):
			if bin(mask[i]).count("1") == 1:
				for j in range(n):
					if i != j and (mask[i] & mask[j]):
						mask[j] ^= mask[i]

	who = map(lambda x: len(bin(x))-3, mask)
	ans = 1
	for i, j in enumerate(who):
		if j < 6:
			ans *= me[i]
	print(ans)

if __name__ == "__main__":
	# part1()
	part2()
