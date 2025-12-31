class Solution(object):
    def isRectangleCover(self, rectangles):
        corners = set()
        total_area = 0
        
        minX = minY = float('inf')
        maxX = maxY = float('-inf')
        
        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)
            
            minX = min(minX, x1)
            minY = min(minY, y1)
            maxX = max(maxX, x2)
            maxY = max(maxY, y2)
            
            for corner in [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        
        if total_area != (maxX - minX) * (maxY - minY):
            return False
        
        expected = {
            (minX, minY),
            (minX, maxY),
            (maxX, minY),
            (maxX, maxY)
        }
        
        return corners == expected

        