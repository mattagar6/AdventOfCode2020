#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<string> g;
	string s;
	while(cin >> s)
		g.push_back(s);
	int n = g.size(), m = g[0].size();
	long long ans = 1, a = 0;
	int i = 0, j = 0;
	while(i < n) {
		if(g[i][j] == '#') 
			a++;
		i += 1;
		j += 1;
		j %= m;
	}
	ans *= a;
	a = 0;
	i = 0, j = 0;
	while(i < n) {
		if(g[i][j] == '#') 
			a++;
		i += 1;
		j += 3;
		j %= m;
	}
	ans *= a;
	a = 0;
	i = 0, j = 0;
	while(i < n) {
		if(g[i][j] == '#') 
			a++;
		i += 1;
		j += 5;
		j %= m;
	}
	ans *= a;
	a = 0;
	i = 0, j = 0;
	while(i < n) {
		if(g[i][j] == '#') 
			a++;
		i += 1;
		j += 7;
		j %= m;
	}
	ans *= a;
	a = 0;
	i = 0, j = 0;
	while(i < n) {
		if(g[i][j] == '#') 
			a++;
		i += 2;
		j += 1;
		j %= m;
	}
	ans *= a;
	a = 0;
	i = 0, j = 0;
	
	cout << ans << endl;
}
