import sys

directions = "NESW"
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def part1():
	
	cur = 1 #current direcion
	x, y = 0, 0
	
	for line in sys.stdin:
		d, amount = line[0], int(line[1:])
		if d in directions:
			for i, ch in enumerate(directions):
				if d == ch:
					x += amount * dx[i]
					y += amount * dy[i]
		elif d == "F":
			x += amount * dx[cur]
			y += amount * dy[cur]
		elif d == "R":
			while amount > 0:
				cur = (cur + 1) % 4
				amount -= 90
		else:
			assert d == "L"
			while amount > 0:
				cur = (cur - 1 + 4) % 4
				amount -= 90
	
	print(abs(x) + abs(y))

def part2():
	
	def rotate(x, y, amount):
		#rotate point x, y amount * 90 degrees counterclockwise
		if amount < 0:
			amount = 4 + amount
		
		for _ in range(amount):
			x, y = -y, x
		
		return x, y
	
	way_x, way_y = 10, 1
	x, y = 0, 0
	for line in sys.stdin:
		d, amount = line[0], int(line[1:])
		if d in directions:
			for i, ch in enumerate(directions):
				if ch == d:
					way_x += amount * dx[i]
					way_y += amount * dy[i]
		elif d == "F":
			vec = way_x - x, way_y - y
			x += amount * vec[0]
			y += amount * vec[1]
			way_x += amount * vec[0]
			way_y += amount * vec[1]
		elif d == "R":
			amount /= 90
			vec = way_x - x, way_y - y
			vec = rotate(vec[0], vec[1], -amount)
			way_x, way_y = x + vec[0], y + vec[1]
		else:
			assert d == "L"
			amount /= 90
			vec = way_x - x, way_y - y
			vec = rotate(vec[0], vec[1], amount)
			way_x, way_y = x + vec[0], y + vec[1]
		
	print(abs(x) + abs(y))
	
if __name__ == "__main__":
	# part1()
	part2()
