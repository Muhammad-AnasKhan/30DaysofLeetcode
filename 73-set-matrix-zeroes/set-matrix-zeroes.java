/*
We initialize two arrays, row and col, to keep track of which rows and columns contain zeros, 
respectively. We iterate through the matrix, and whenever we encounter a zero at position (i, j), 
we mark the ith row and jth column as containing zeros by setting row[i] and col[j] to 1.

After marking all the rows and columns containing zeros, we iterate through the matrix again. 
For each element (i, j) in the matrix, if either row[i] or col[j] is 1, we set the element to zero.
*/
class Solution {
    public void setZeroes(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int [] row = new int[n];
        int [] col = new int[m];
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(matrix[i][j] == 0){
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(row[i] == 1 || col[j] == 1){
                    matrix[i][j] = 0;
                }
            }
        }
    }
}