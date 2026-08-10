class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, current):
            # Add the current subset
            result.append(current[:])

            for i in range(start, len(nums)):
                # Include nums[i]
                current.append(nums[i])

                # Explore next elements
                backtrack(i + 1, current)

                # Backtrack
                current.pop()

        backtrack(0, [])

        return result