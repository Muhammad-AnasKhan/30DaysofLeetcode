class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        n, m = len(board), len(board[0])
        
        def word_exists(row, col, p):
            if p == len(word):
                return True
                
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ci, cj = i + row, j + col
                if 0 <= ci < n and  0 <= cj < m and (ci, cj) not in vis and board[ci][cj] == word[p]:
                    vis.add((ci, cj))
                    if word_exists(ci, cj, p+1):
                        return True
                    
                    vis.remove((ci, cj))
                    
            return False
                    
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    vis.add((i, j))
                    if word_exists(i, j, 1):
                        return True
                    vis.remove((i, j))
                
        return False