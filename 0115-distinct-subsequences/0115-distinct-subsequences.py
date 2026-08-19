class Solution:
    def numDistinct(self, s, t):

        m = len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (m + 1)

        # Empty string can be formed in exactly one way
        dp[0] = 1

        for ch in s:

            # Go backwards to avoid overwriting dp[j-1]
            for j in range(m, 0, -1):

                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]