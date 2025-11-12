class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to count character frequencies
        count = {}

        # First pass: count occurrences of each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Second pass: find first character with frequency 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        # If no unique character found
        return -1

        