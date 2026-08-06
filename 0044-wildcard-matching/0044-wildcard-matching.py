class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        # dp[j] = whether current prefix of s matches p[:j]
        dp = [False] * (n + 1)
        dp[0] = True

        # Empty string vs pattern
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]
            else:
                break

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = False

            for j in range(1, n + 1):
                temp = dp[j]

                if p[j - 1] == '*':
                    # '*' matches empty OR one/more characters
                    dp[j] = dp[j - 1] or dp[j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[j] = prev
                else:
                    dp[j] = False

                prev = temp

        return dp[n]