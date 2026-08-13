class Solution {
    void fun(char[][] g, int i, int j){
        if(i<0 || j<0 || i>= g.length || j>= g[0].length) return;
        if(g[i][j] == '0') return;
        g[i][j] = '0';
        fun(g,i-1,j);
        fun(g,i,j-1);
        fun(g,i+1,j);
        fun(g,i,j+1);
    }
    public int numIslands(char[][] g) {
        int c =0;
        for(int i=0;i<g.length;i++){
            for(int j=0;j<g[0].length;j++){
                if(g[i][j] == '1'){
                    fun(g, i , j);
                    c++;
                }
            }
        }
        return c;
    }
}