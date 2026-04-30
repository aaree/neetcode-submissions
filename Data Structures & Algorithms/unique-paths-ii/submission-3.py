class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        rObs=False
        cObs=False
        for i in range(r):
            for j in range(c):
                if (i==0) and obstacleGrid[i][j]!=1 and (not cObs):
                    obstacleGrid[i][j]=1
                elif (j==0) and not rObs and obstacleGrid[i][j]!=1:
                    obstacleGrid[i][j]=1
                elif obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=-1
                    if i==0:
                        cObs=True
                    if j==0:
                        rObs=True
        print(obstacleGrid)
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i-1][j]<0:
                    up=0
                else:
                    up=obstacleGrid[i-1][j]
                if obstacleGrid[i][j-1]<0:
                    left=0
                else:
                    left=obstacleGrid[i][j-1]
                if obstacleGrid[i][j]>=0:
                    obstacleGrid[i][j]=up+left
        return obstacleGrid[r-1][c-1]