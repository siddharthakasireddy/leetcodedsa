import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: store start points with their original indices
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        start_points = [s[0] for s in starts]  # Extract just start values
        result = []

        # Step 2: For each interval, binary search for the smallest start >= end
        for start, end in intervals:
            idx = bisect.bisect_left(start_points, end)  # Find insertion point
            if idx < len(intervals):
                result.append(starts[idx][1])  # append index of that interval
            else:
                result.append(-1)  # No valid right interval
        return result

        