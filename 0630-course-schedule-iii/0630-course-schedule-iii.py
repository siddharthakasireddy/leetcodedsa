import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        total = 0
        maxHeap = []

        for d, end in courses:
            total += d
            heapq.heappush(maxHeap, -d)
            if total > end:
                total += heapq.heappop(maxHeap)

        return len(maxHeap)

        