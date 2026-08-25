class Solution:
    def trailingZeroes(self, n):
        ans = 0

        while n >= 5:
            n = n // 5
            ans = ans + n

        return ans