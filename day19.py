import copy
import sys

def part2():
	lines = [line.strip() for line in sys.stdin]
	g = {x: [] for x in range(200)}
	res = {x: set() for x in range(200)}
	vec = {x: [] for x in range(200)}
	
	ptr = 0
	N = len(lines)
	while ptr < N:
		line = lines[ptr]
		if not line:
			ptr += 1
			break
		l = line.split(":")
		me, rest = int(l[0]), l[1].strip()
		for x in rest.split():
			if x[0].isdigit() and int(x) != me:
				g[me].append(int(x))
			elif x != "|" and not x[0].isdigit():
				res[me].add(x[1])
		
		if "|" in rest:
			zz = rest.split("|")
			for i in range(2):
				zz[i] = zz[i].strip()
			vec[me] = [list(map(int, zz[i].split())) for i in range(2)]
		elif rest[0].isdigit():
			vec[me] = [list(map(int, rest.split()))]
		ptr += 1
	
	vis = set()
	def dfs(u, topo):
		vis.add(u)
		for v in g[u]:
			if v not in vis:
				dfs(v, topo)
		topo.append(u)
		
	topo = []
	dfs(0, topo)
	
	ans = 0
	for i in range(ptr, N):
		line = lines[i]
		m = len(line)
		valid = set()
		for j in range(0, m):
			for k in range(j, m):
				valid.add(line[j:k+1])
		
		zzz = copy.deepcopy(res)
		for u in topo:
			if res[u]:
				continue
			for move in vec[u]:
				if len(move) == 1:
					for a in res[move[0]]:
						res[u].add(a)
				elif move != [42, 8] and move != [42, 11, 31]:
					assert len(move) == 2
					for a in res[move[0]]:
						for b in res[move[1]]:
							if a+b in valid:
								res[u].add(a + b)
			if u == 8:
				f = True
				while f:
					f = False
					tmp = set(s for s in res[u])
					for a in res[u]:
						for b in res[u]:
							if a+b not in tmp and a+b in valid:
								f = True
								tmp.add(a+b)
					res[u] = tmp
			
			if u == 11:
				f = True
				while f:
					f = False
					tmp = set(s for s in res[u])
					for a in res[42]:
						for b in res[u]:
							for c in res[31]:
								if a+b+c not in tmp and a+b+c in valid:
									f = True
									tmp.add(a+b+c)
					res[u] = tmp
		
		if line in res[0]:
			ans += 1

		res = zzz

	print(ans)
	
if __name__ == "__main__":
	part2()
