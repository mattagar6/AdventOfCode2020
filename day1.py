import sys

def part1():
	nums = set()

	for line in sys.stdin:
		x = int(line)
		if 2020 - x in nums:
			print(x * (2020 - x))
			break
		nums.add(x)

def part2():
	
	nums = list(map(int, [line for line in sys.stdin]))
	nums.sort()
	n = len(nums)
	
	for i, x in enumerate(nums):
		want = 2020 - x
		j = i+1
		k = n-1
		while j < k:
			if nums[j] + nums[k] == want:
				print(nums[i] * nums[j] * nums[k])
				break
			elif nums[j] + nums[k] < want:
				j += 1
			else:
				k -= 1
	
	
if __name__ == "__main__":
	# part1()
	part2()
