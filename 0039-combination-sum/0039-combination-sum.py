class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                # Choose the number
                current.append(num)

                # i instead of i + 1 because
                # the same number can be reused
                backtrack(i, remaining - num, current)

                # Backtrack
                current.pop()

        candidates.sort()
        backtrack(0, target, [])

        return result