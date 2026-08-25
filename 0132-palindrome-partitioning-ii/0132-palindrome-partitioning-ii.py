class Solution:
    def minCut(self, s):
        n = len(s)

        if n <= 1:
            return 0

        # dp[i] = minimum cuts needed for s[0:i+1]
        cuts = list(range(n))

        # palindrome[i][j] tells whether s[i:j+1] is a palindrome
        palindrome = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):

                if s[start] == s[end] and (
                    end - start <= 2 or palindrome[start + 1][end - 1]
                ):
                    palindrome[start][end] = True

                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(
                            cuts[end],
                            cuts[start - 1] + 1
                        )

        return cuts[n - 1]