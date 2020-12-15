import sys
input = sys.stdin.readline

def main():
	vec = list(map(int, input().split(",")))
	where = {}
	for i, x in enumerate(vec):
		where[x] = [i]
	
	print(where)
	for i in range(len(vec), 30000000):
		prv = vec[-1]
		# print(prv)
		if len(where[prv]) == 1:
			vec.append(0)
			if 0 not in where:
				where[0] = [i]
			else:
				where[0].append(i)
		else:
			d = where[prv][-1] - where[prv][-2]
			vec.append(d)
			if d in where:
				where[d].append(i)
			else:
				where[d] = [i]
	
	print(vec[-1])

if __name__ == "__main__":
	main()
