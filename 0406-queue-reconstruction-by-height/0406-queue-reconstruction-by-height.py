class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Step 1: Sort by height descending, then by k ascending
        # -p[0] makes height descending, p[1] makes k ascending
        people.sort(key=lambda p: (-p[0], p[1]))
        
        queue = []
        
        # Step 2: Insert each person into the queue at index k
        for person in people:
            queue.insert(person[1], person)
            
        return queue
        