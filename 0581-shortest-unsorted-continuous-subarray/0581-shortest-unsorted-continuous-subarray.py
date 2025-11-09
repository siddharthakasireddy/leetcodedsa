class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = -1, -2   # default values if array is already sorted
        min_val, max_val = nums[-1], nums[0]

        # Traverse from left to right to find the right boundary
        for i in range(1, n):
            max_val = max(max_val, nums[i])
            if nums[i] < max_val:
                end = i

        # Traverse from right to left to find the left boundary
        for i in range(n - 2, -1, -1):
            min_val = min(min_val, nums[i])
            if nums[i] > min_val:
                start = i

        return end - start + 1

        