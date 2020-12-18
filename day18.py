import sys

def go(s):
	stk = []
	op = "+"
	cur = 0
	for ch in s:
		if ch == "(":
			stk.append((op, cur))
			op = "+"
			cur = 0
		elif ch == ")":
			op, val = stk.pop()
			cur = cur + val if op == "+" else cur * val
		elif ch.isdigit():
			cur = int(ch) + cur if op == "+" else int(ch) * cur
		else:
			op = ch
			
	return cur

def part1():
	exp = list(map(lambda line: "".join(line.strip().split()), [line for line in sys.stdin]))
	print(sum(go(e) for e in exp))

def part2():
	
	def fix(s):
		t = ["("]
		bal = 1
		for ch in s:
			if ch == "*":
				t.append(")")
				bal -= 1
			if ch == "(":
				t.append("(")
				bal += 2
			elif ch == ")":
				t.append(")")
				bal -= 2
			
			t.append(ch)
			
			if ch == "*":
				t.append("(")
				bal += 1
		
		t.append(")")
		assert bal == 1
		return "".join(t)
	
	exp = list(map(lambda line: fix("".join(line.strip().split())), [line for line in sys.stdin]))
	print(sum(go(e) for e in exp))

if __name__ == "__main__":
	# part1()
	part2()
