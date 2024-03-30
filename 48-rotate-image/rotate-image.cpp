// swap[ basically transpose of a matrix ]
// Finally reverse each array of the matrix

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
         int n = matrix.size();
        
        // Take a tranpose of the matrix
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        // Reverse each row of the matrix to get the output
        for(int i=0; i<n; i++){
            reverse(matrix[i].begin(), end(matrix[i]));
        }
    }
};