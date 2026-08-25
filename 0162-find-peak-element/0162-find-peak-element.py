class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # We are on the decreasing side.
                # A peak exists at mid or to the left.
                right = mid
            else:
                # We are on the increasing side.
                # A peak exists to the right.
                left = mid + 1

        return left