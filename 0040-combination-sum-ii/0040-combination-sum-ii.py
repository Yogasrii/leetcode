class Solution:
    def combinationSum2(self, candidates, target):
        result = []

        candidates.sort()

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1,
                          remaining - candidates[i],
                          current)

                current.pop()

        backtrack(0, target, [])

        return result