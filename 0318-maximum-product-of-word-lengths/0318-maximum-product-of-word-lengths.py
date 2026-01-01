class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        masks = [0] * n
        lengths = [len(w) for w in words]

        # Build bitmask for each word
        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask

        max_prod = 0

        # Compare all pairs
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:  # no common letters
                    max_prod = max(max_prod, lengths[i] * lengths[j])

        return max_prod

        