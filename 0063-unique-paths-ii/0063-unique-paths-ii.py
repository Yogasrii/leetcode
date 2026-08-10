class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n

        # Starting position
        dp[0] = 1

        for i in range(m):
            for j in range(n):

                # If current cell is an obstacle
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0

                else:
                    # Add paths from the left
                    if j > 0:
                        dp[j] += dp[j - 1]

        return dp[n - 1]