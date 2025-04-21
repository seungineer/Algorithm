import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] dir = new int[][] {
		{1,0},{1,1},{0,1},{-1,1},
		{-1,0},{-1,-1},{0,-1},{1,-1}
	};
	static int[][] distanceMap;
	static int[][] map;
	
	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = pint(st.nextToken());
		int m = pint(st.nextToken());
		map = new int[n][m];
		distanceMap = new int[n][m];
		
		for(int i = 0; i < map.length; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < map[0].length; j++) {
				map[i][j] = pint(st.nextToken());
				distanceMap[i][j] = Integer.MAX_VALUE;
			}
		}

		int ans = 0;
		for(int i = 0; i < map.length; i++) {
			for(int j = 0; j < map[0].length; j++) {
				if(map[i][j]==1) {
					dfs(i,j);
				}
			}
		}

		for(int i=0; i<map.length; i++) {
			for(int j=0; j<map[0].length; j++) {
				if(ans<distanceMap[i][j])ans=distanceMap[i][j];
			}
		}
		System.out.println(ans);
	}
	
	static void dfs(int x, int y) {
		Queue<point>qu = new LinkedList<>(); 
		qu.offer(new point(x,y,0));
		distanceMap[x][y] = 0;
		
		while(!qu.isEmpty()) {
			point cur = qu.poll();
			
			for(int d=0;d<dir.length;d++) {
				int nx = cur.x + dir[d][0];
				int ny = cur.y + dir[d][1];
				int depth = cur.depth + 1;
				
				if(nx<0 || nx >= map.length || ny<0 || ny>=map[0].length || distanceMap[nx][ny]<=depth) {
					continue;
				}
				
				distanceMap[nx][ny] = depth;
				qu.offer(new point(nx,ny,depth));
			}
		}
	}
	
	static int pint(String s) {
		return Integer.parseInt(s);
	}
	

}

class point{
	int x;
	int y;
	int depth;
	public point(int x, int y, int depth) {
		super();
		this.x = x;
		this.y = y;
		this.depth = depth;
	}
}