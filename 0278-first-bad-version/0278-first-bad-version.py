class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid   # first bad version is at mid or before
            else:
                left = mid + 1  # first bad version is after mid
        
        return left

        