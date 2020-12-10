import sys

def part1():
	nums = [0] + sorted(list(map(int, [line for line in sys.stdin])))
	diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
	print(diffs.count(1) * (diffs.count(3) + 1))

def part2():
	nums = [0] + sorted(list(map(int, [line for line in sys.stdin])))
	nums += [nums[-1] + 3]
	n = len(nums)
	dp = [0]*(n)
	dp[0] = 1
	for i in range(1, n):
		for j in range(max(0, i-3), i):
			if nums[j] + 3 >= nums[i]:
				dp[i] += dp[j]
	print(dp[-1])


if __name__ == "__main__":
	# part1()
	part2()
	
