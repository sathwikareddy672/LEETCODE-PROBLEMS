class Solution {
    boolean ans = false;
    void find(char [][] mat, int i, int j, int idx, String s){
        if(idx >= s.length()){
            ans = true;
            return;
        }
        if(i < 0 || j < 0 || i >= mat.length || j >= mat[0].length) return;
        if(s.charAt(idx) != mat[i][j]) return;
        char temp = mat[i][j];
        mat[i][j] = '&';
        find(mat, i+1, j, idx+1, s);
        find(mat, i-1, j, idx+1, s);
        find(mat, i, j+1, idx+1, s);
        find(mat, i, j-1, idx+1, s);
        mat[i][j] = temp;
    }
    public boolean exist(char[][] mat, String s) {
        for (int i = 0; i < mat.length; i++ ){
            for (int j = 0; j < mat[i].length; j++){
                if(s.charAt(0) == mat[i][j]){
                    find(mat, i, j, 0, s);
                }
            }
        }
        return ans;
    }
}