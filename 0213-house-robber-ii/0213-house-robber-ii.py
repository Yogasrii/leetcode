class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev = 0
            curr = 0

            for money in houses:
                new_curr = max(curr, prev + money)
                prev = curr
                curr = new_curr

            return curr

        # Case 1: Exclude last house
        case1 = rob_linear(nums[:-1])

        # Case 2: Exclude first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)