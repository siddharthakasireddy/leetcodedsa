class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Number of papers that have at least citations[mid] citations
            h = n - mid
            if citations[mid] == h:
                return h
            elif citations[mid] < h:
                left = mid + 1
            else:
                right = mid - 1
                
        return n - left

        