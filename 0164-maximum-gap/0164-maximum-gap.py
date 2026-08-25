class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Minimum possible maximum gap
        gap = (max_val - min_val + n - 2) // (n - 1)

        bucket_min = [float('inf')] * n
        bucket_max = [float('-inf')] * n
        used = [False] * n

        # Put numbers into buckets
        for num in nums:
            index = (num - min_val) // gap

            if index >= n:
                index = n - 1

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
            used[index] = True

        # Find maximum gap between buckets
        answer = 0
        previous = min_val

        for i in range(n):
            if not used[i]:
                continue

            answer = max(answer, bucket_min[i] - previous)
            previous = bucket_max[i]

        return answer