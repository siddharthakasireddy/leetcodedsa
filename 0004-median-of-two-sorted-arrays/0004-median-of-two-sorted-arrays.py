class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Ensure A is the smaller array
        if m > n:
            A, B, m, n = B, A, n, m

        low, high = 0, m
        half = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2   # partition in A
            j = half - i            # partition in B

            A_left = A[i-1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j-1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            # correct partition found
            if A_left <= B_right and B_left <= A_right:
                # odd length
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                # even length
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                high = i - 1
            else:
                low = i + 1

        