class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array first
        result = []  # To store the result
        
        for i in range(len(nums) - 2):
            # Skip duplicate elements for the `i`th position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:  # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    # Move the left pointer to the next distinct element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the previous distinct element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move both pointers
                    left += 1
                    right -= 1
                elif total < 0:  # We need a larger sum, move the left pointer
                    left += 1
                else:  # We need a smaller sum, move the right pointer
                    right -= 1
        
        return result

        