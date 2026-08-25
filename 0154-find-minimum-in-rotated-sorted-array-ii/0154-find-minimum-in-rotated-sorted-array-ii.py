class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is on the right side
                left = mid + 1

            elif nums[mid] < nums[right]:
                # Minimum is at mid or on the left side
                right = mid

            else:
                # nums[mid] == nums[right]
                # We cannot determine the side,
                # so safely remove the duplicate right value
                right -= 1

        return nums[left]