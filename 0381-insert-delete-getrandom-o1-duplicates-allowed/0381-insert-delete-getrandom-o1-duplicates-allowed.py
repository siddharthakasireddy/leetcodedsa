import random

class RandomizedCollection(object):

    def __init__(self):
        self.nums = []                # List to store all values
        self.indices = {}             # Map from val -> set of indices

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        is_new = val not in self.indices
        if is_new:
            self.indices[val] = set()
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        return is_new

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indices or not self.indices[val]:
            return False
        
        # Get an arbitrary index of val to remove
        remove_idx = self.indices[val].pop()
        last_val = self.nums[-1]

        # Move last element into the removed spot (if not same)
        if remove_idx != len(self.nums) - 1:
            self.nums[remove_idx] = last_val
            # Update the index set for last_val
            self.indices[last_val].remove(len(self.nums) - 1)
            self.indices[last_val].add(remove_idx)
        
        # Remove last element
        self.nums.pop()

        # Clean up if val no longer present
        if not self.indices[val]:
            del self.indices[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)
