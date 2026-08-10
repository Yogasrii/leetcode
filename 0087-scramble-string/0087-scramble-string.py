class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def solve(a, b):
            # Already calculated
            if (a, b) in memo:
                return memo[(a, b)]

            # Strings are equal
            if a == b:
                memo[(a, b)] = True
                return True

            # Different characters -> impossible
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)

            # Try every possible split
            for i in range(1, n):

                # Case 1: No swap
                if (solve(a[:i], b[:i]) and
                    solve(a[i:], b[i:])):
                    memo[(a, b)] = True
                    return True

                # Case 2: Swap
                if (solve(a[:i], b[n-i:]) and
                    solve(a[i:], b[:n-i])):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return solve(s1, s2)