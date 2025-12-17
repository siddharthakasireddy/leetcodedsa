import heapq

class Solution(object):
    def getSkyline(self, buildings):
        events = []
        
        for l, r, h in buildings:
            events.append((l, -h))  # building start
            events.append((r, h))   # building end
        
        events.sort()
        
        result = []
        heap = [0]
        active = {0: 1}
        prev_max = 0
        
        for x, h in events:
            if h < 0:  # start of building
                heapq.heappush(heap, h)
                active[-h] = active.get(-h, 0) + 1
            else:  # end of building
                active[h] -= 1
            
            while heap and active[-heap[0]] == 0:
                heapq.heappop(heap)
            
            curr_max = -heap[0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max
        
        return result

        