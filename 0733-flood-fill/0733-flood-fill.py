class Solution:
    def floodFill(self, image, sr, sc, color):
        
        def dfs(sr, sc, image, color, n, m):
            for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr = sr + r
                nc = sc + c
                
                if (nr >= 0 and nr < n and nc >= 0 and nc < m and 
                    image[nr][nc] == dl):
                    
                    image[nr][nc] = color
                    dfs(nr, nc, image, color, n, m)

        # If the starting pixel already has the target color
        if color == image[sr][sc]:
            return image
        
        n = len(image)
        m = len(image[0])
        
        dl = image[sr][sc]
        image[sr][sc] = color
        
        dfs(sr, sc, image, color, n, m)
        
        return image