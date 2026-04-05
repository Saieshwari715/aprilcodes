class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dir=[(0,-1),(1,0),(0,1),(-1,0)]
        def fun(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]='0'
            while q:
                sr,sc=q.popleft()
                for i,j in dir:
                    nr,nc=sr+i,sc+j
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]=='1':
                        q.append((nr,nc))
                        grid[nr][nc]='0'



                        

                     
        co=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    co+=1
                    fun(r,c)
                    
                    
        return co













        '''if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        islands=0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0":
                return
            grid[r][c]="0"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]=="1"):
                    islands+=1
                    dfs(r,c)
        return islands'''

