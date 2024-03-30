// swap[ basically transpose of a matrix ]
// Finally reverse each array of the matrix

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
         int N=matrix.size();
		//transpose of matrix
        for (int i = 0; i < N; i++) 
			for (int j = i+1; j < N; j++) 
				swap(matrix[i][j], matrix[j][i]);
                
		//swap elements of each rows 
        for (int i = 0; i < N; i++) 
			for (int j = 0, k = N - 1;j < k; j++, k--) 
				swap(matrix[i][j], matrix[i][k]); 
    }
};