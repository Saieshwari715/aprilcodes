class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dir=[(0,-1),(1,0),(0,1),(-1,0)]
        maxi=0
        def fun(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]=0
            a=1
            while q:
                
                sr,sc=q.popleft()
                
                for i,j in dir:
                    nr,nc=sr+i,sc+j
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=0
                        a+=1
            return a
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    
                    maxi=max(maxi,fun(r,c))
                    
         
        return maxi














