import sys

keys = ["byr", #(Birth Year)
		"iyr", #(Issue Year)
		"eyr", #(Expiration Year)
		"hgt", #(Height)
		"hcl", #(Hair Color)
		"ecl", #(Eye Color)
		"pid", #(Passport ID)
		# "cid"  #(Country ID)
		]
		
BLANK = "\n"

def part1():
	ans = 0
	cur = ""
	for line in sys.stdin:
		if line == BLANK:
			fields = {s.split(":")[0] for s in cur.split()}
			if all(key in fields for key in keys):
				ans += 1
			cur = ""
		else:
			cur += line[:-1] + " "
	print(ans)

def part2():
	ans = 0
	cur = ""
	for line in sys.stdin:
		if line == BLANK:
			fields = {s.split(":")[0] : s.split(":")[1] for s in cur.split()}
			cur = ""
			if all(key in fields.keys() for key in keys):
				if int(fields["byr"]) < 1920 or int(fields["byr"]) > 2002:
					continue
				if int(fields["iyr"]) < 2010 or int(fields["iyr"]) > 2020:
					continue
				if int(fields["eyr"]) < 2020 or int(fields["eyr"]) > 2030:
					continue
				
				if fields["hgt"][-2:] == "cm":
					if int(fields["hgt"][:-2]) < 150 or int(fields["hgt"][:-2]) > 193:
						continue
				else:
					if int(fields["hgt"][:-2]) < 59 or int(fields["hgt"][:-2]) > 76:
						continue
				
				if fields["hcl"][0] != "#" or any(c not in "1234567890abcdef" for c in fields["hcl"][1:]):
					continue
				if fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
					continue
				
				if len(fields["pid"]) != 9 or any(not c.isdigit() for c in fields["pid"]):
					continue
					
				ans += 1
			
		else:
			cur += line[:-1] + " "
	print(ans)

if __name__ == "__main__":
	# part1()
	part2()
