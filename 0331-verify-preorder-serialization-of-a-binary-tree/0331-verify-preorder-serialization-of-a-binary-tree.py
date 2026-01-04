class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1  # initial slot for root
        
        for node in preorder.split(','):
            # consume one slot
            slots -= 1
            
            # if no slot available, invalid
            if slots < 0:
                return False
            
            # non-null node creates two new slots
            if node != '#':
                slots += 2
        
        # all slots must be exactly used
        return slots == 0

        