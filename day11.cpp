#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const int MAXN = 1000;

char grid[2][MAXN][MAXN];
int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int n, m;

void read() {
	string s;
	while(cin >> s) {
		m = s.size();
		for(int i = 0; i < m; i++)
			grid[0][n][i] = s[i];
		n++;
	}
}

bool valid(int i, int j) {
	return 0 <= i && i < n && 0 <= j && j < m;
}

void part1() {
	int z = 0;
	bool anything = true;
	for(; anything; z ^= 1) {
		memcpy(grid[z^1], grid[z], sizeof grid[z]);
		anything = false;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				int cnt = 0;
				for(int k = 0; k < 8; k++) {
					int r = i + dr[k], c = j + dc[k];
					if(valid(r, c) && grid[z][r][c] == '#')
						cnt++;
				}
			
				if(grid[z][i][j] == 'L' && cnt == 0) {
					grid[z^1][i][j] = '#';
					anything = true;
				}
				else if(grid[z][i][j] == '#' && cnt >= 4) {
					grid[z^1][i][j] = 'L';
					anything = true;
				}
			}
		}
	}
	
	int ans = 0;
	for(int i = 0; i < n; i++) 
		for(int j = 0; j < m; j++)
			ans += grid[z][i][j] == '#';
	cout << ans << endl;
}

void part2() {
	int z = 0;
	bool anything = true;
	for(; anything; z ^= 1) {
		memcpy(grid[z^1], grid[z], sizeof grid[z]);
		anything = false;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				int cnt = 0;
				for(int k = 0; k < 8; k++) {
					int r = i + dr[k], c = j + dc[k];
					while(valid(r, c) && grid[z][r][c] == '.') {
						r += dr[k], c += dc[k];
					}
					if(valid(r, c) && grid[z][r][c] == '#')
						cnt++;
				}
			
				if(grid[z][i][j] == 'L' && cnt == 0) {
					grid[z^1][i][j] = '#';
					anything = true;
				}
				else if(grid[z][i][j] == '#' && cnt >= 5) {
					grid[z^1][i][j] = 'L';
					anything = true;
				}
			}
		}
	}
	
	int ans = 0;
	for(int i = 0; i < n; i++) 
		for(int j = 0; j < m; j++)
			ans += grid[z][i][j] == '#';
	cout << ans << endl;
}

int main() {

	read();
	//part1();
	part2();
	
}
