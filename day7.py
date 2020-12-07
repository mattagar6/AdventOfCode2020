import sys
import string

def part1():
	
	g = {}
	for line in sys.stdin:
		line = line.translate(None, string.punctuation)
		if "no other bags" in line:
			continue
			
		l = []
		outer = None
		for s in line.split():
			if s in {"bag", "bags"}:
				cur = l[-2] + " " + l[-1]
				if outer is None:
					outer = cur
				else:
					if outer not in g:
						g[outer] = [cur]
					else:
						g[outer] += [cur]
			l += [s]
	
	
	vis = set()
	def toposort(u, topo):
		vis.add(u)
		if u not in g:
			topo += [u]
			return
			
		for v in g[u]:
			if v not in vis:
				toposort(v, topo)
		
		topo += [u]
	
	topo = []
	for color in g.keys():
		if color not in vis:
			toposort(color, topo)

	dp = {}
	
	for u in topo:
		dp[u] = int(u == "shiny gold")
		if u not in g:
			continue
		for v in g[u]:
			dp[u] |= dp[v]
	
	print(sum(x for x in dp.values()) - 1)

def part2():
	
	g = {}
	for line in sys.stdin:
		line = line.translate(None, string.punctuation)
		if "no other bags" in line:
			continue
			
		l = []
		outer = None
		cnt = -1
		for s in line.split():
			if s in {"bag", "bags"}:
				cur = l[-2] + " " + l[-1]
				if outer is None:
					outer = cur
				else:
					if outer not in g:
						g[outer] = [(cur, cnt)]
					else:
						g[outer] += [(cur, cnt)]
			if s[0].isdigit():
				cnt = int(s)
			l += [s]

	vis = set()
	def toposort(u, topo):
		vis.add(u)
		if u not in g:
			topo += [u]
			return
			
		for v, _ in g[u]:
			if v not in vis:
				toposort(v, topo)
		
		topo += [u]
	
	topo = []
	for color in g.keys():
		if color not in vis:
			toposort(color, topo)
	
	dp = {}
	
	for u in topo:
		dp[u] = 1
		if u not in g:
			dp[u] = 1
			continue
		for v, cnt in g[u]:
			dp[u] += cnt * dp[v]
	
	print(dp["shiny gold"] - 1)

if __name__ == "__main__":
	# part1()
	part2()
