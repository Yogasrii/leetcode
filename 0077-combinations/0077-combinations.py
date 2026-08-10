class Solution:
    def combine(self, n, k):
        result = []

        def backtrack(start, current):
            # Combination is complete
            if len(current) == k:
                result.append(current[:])
                return

            # Try all possible numbers
            for num in range(start, n + 1):
                current.append(num)

                backtrack(num + 1, current)

                # Backtrack
                current.pop()

        backtrack(1, [])

        return result