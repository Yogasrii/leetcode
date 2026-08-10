class Solution:
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            
            # If current index cannot be reached
            if i > max_reach:
                return False

            # Update the farthest position we can reach
            max_reach = max(max_reach, i + nums[i])

            # If we can reach the last index
            if max_reach >= len(nums) - 1:
                return True

        return True