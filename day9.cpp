#include <iostream>
#include <map>
using namespace std;

const int MAXN = 50'000;

long long qu[MAXN], qs, missing;

void part1() {
	for(int i = 0; i < 25; i++)
		cin >> qu[qs++];
	
	long long x;
	while(cin >> x) {
		bool found = false;
		for(int i = qs - 25; i < qs; i++)
			for(int j = i+1; j < qs; j++)
				if(qu[i] + qu[j] == x)
					found = true;
		if(!found)
			missing = x;
		qu[qs++] = x;
	}
	
	cout << missing << endl;
}

void part2() {
	long long sum = 0;
	map<long long, int> where;
	where[sum] = -1;
	
	for(int i = 0; i < qs; i++) {
		sum += qu[i];
		if(where.count(sum - missing) && where[sum - missing] + 1 < i) {
			int j = where[sum - missing] + 1;
			long long lo = qu[j], hi = qu[j];
			for(int k = j; k <= i; k++)
				lo = min(lo, qu[k]), hi = max(hi, qu[k]);
			cout << lo + hi << "\n";
		}
		where[sum] = i;
	}
}

int main() {
	part1();
	part2();
}
