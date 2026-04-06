class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        di=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        
        q=deque()
        q.append((0,0,1))
        grid[0][0]=0
        while q:
                r,c,st=q.popleft()
                if r==n-1 and c==n-1:
                    return st
                for i,j in di:
                    nr,nc=r+i,c+j
                   
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                        q.append((nr,nc,st+1))
                        grid[nr][nc]=1
        return -1









        