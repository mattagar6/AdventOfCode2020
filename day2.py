import sys

def part1():
	ans = 0
	for line in sys.stdin:
		times, letter, password = line.split()
		low, high = map(int, times.split("-"))
		if low <= password.count(letter[0]) <= high:
			ans += 1
		
	print(ans)

def part2():
	ans = 0
	for line in sys.stdin:
		times, letter, password = line.split()
		i, j = map(lambda x: int(x)-1, times.split("-"))
		if int(password[i] == letter[0]) ^ int(password[j] == letter[0]):
			ans += 1
		
	print(ans)
	
if __name__ == "__main__":
	# part1()
	part2()
