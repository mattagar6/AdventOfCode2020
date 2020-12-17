#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const int MAXN = 50;
const int OFFSET = MAXN/2;

int n, g[2][MAXN][MAXN][MAXN][MAXN], p;
string in[MAXN];

void part2() {
	const int turns = 6;
	for(int rep = 0; rep < turns; rep++) {
		memcpy(g[p^1], g[p], sizeof g[p]);
		
		for(int x = 1; x < MAXN-1; x++) {
			for(int y = 1; y < MAXN-1; y++) {
				for(int z = 1; z < MAXN-1; z++) {
					for(int w = 1; w < MAXN-1; w++) {
						int nei = 0;
						for(int dx = -1; dx <= 1; dx++)
							for(int dy = -1; dy <= 1; dy++)
								for(int dz = -1; dz <= 1; dz++) 
									for(int dw = -1; dw <= 1; dw++)
										if(dx || dy || dz || dw)
											nei += g[p][x+dx][y+dy][z+dz][w+dw];
						if(g[p][x][y][z][w] && (nei < 2 || nei > 3))
							g[p^1][x][y][z][w] = 0;
						if(!g[p][x][y][z][w] && nei == 3)
							g[p^1][x][y][z][w] = 1;
					}
				}
			}
		}
		
		p ^= 1;
	}
	int ans = 0;
	for(int a = 0; a < MAXN; a++)	
		for(int b = 0; b < MAXN; b++)
			for(int c = 0; c < MAXN; c++)
				for(int d = 0; d < MAXN; d++)
					ans += g[p][a][b][c][d];
	cout << ans << endl;
}

int main() {
	
	while(getline(cin, in[n++]));

	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			g[p][i+OFFSET][j+OFFSET][OFFSET][OFFSET] = in[i][j] == '#';
		}
	}
	part2();
}	
