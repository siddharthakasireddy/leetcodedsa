class Solution(object):
    def findDisappearedNumbers(self, nums):
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res

        