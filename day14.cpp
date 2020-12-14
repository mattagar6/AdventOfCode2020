#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100*1000;
const int B = 36;
long long mem[MAXN];
string mask;


void part1() {
	string line;
	while(getline(cin, line)) {
		if(line.substr(0, 3) == "mem") {
			int idx = 0;
			for(int i = 4; ; i++) {
				if(line[i] == ']') {
					long long v = stoll(line.substr(i+4));
					mem[idx] = 0;
					for(int j = 0; j < B; j++) {
						if(mask[j] ^ 'X') {
							mem[idx] ^= (mask[j]-'0'*1LL)<<(B-1-j);
						}
						else {
							mem[idx] ^= (v>>(B-1-j)&1LL)<<(B-1-j);
						}
					}
					break;
				}
				else {
					idx = 10 * idx + (line[i]-'0');
				}
			}
		}
		else {
			mask = line.substr(7);
		}
	}
	
	long long sum = 0;
	for(int i = 0; i < MAXN; i++)
		sum += mem[i];
		
	cout << sum << endl;
}

void part2() {
	string line;
	long long mask1 = 0, mask2 = 0;
	map<long long,long long> mp;
	while(getline(cin, line)) {
		if(line.substr(0, 3) == "mem") {
			long long idx = 0;
			for(int i = 4; ; i++) {
				if(line[i] == ']') {
					for(int j = 0; j < B; j++) {
						if(mask1>>j&1)	
							idx |= 1LL<<j;
					}
					long long v = stoll(line.substr(i+4));
					for(long long sub = mask2; ; sub = (sub - 1) & mask2) {
						mp[idx ^ sub] = v;
						
						if(!sub) {
							break;
						}
					}
					
					break;
				}
				else {
					idx = 10 * idx + (line[i]-'0');
				}
			}
		}
		else {
			mask1 = mask2 = 0;
			line = line.substr(7);
			for(int i = 0; i < B; i++) {
				if(line[i] ^ 'X') {
					mask1 ^= (line[i]-'0'*1LL)<<(B-1-i);
				}
				else {
					mask2 ^= 1LL<<(B-1-i);
				}
			}
		}
	}
	
	long long sum = 0;
	for(auto& p : mp)
		sum += p.second;
		
	cout << sum << endl;
}

int main() {
	//part1();
	part2();
}
