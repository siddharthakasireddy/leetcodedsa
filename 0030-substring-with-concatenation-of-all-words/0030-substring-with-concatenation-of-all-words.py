class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        w = len(words[0])          # length of each word
        k = len(words)             # number of words
        total = w * k              # total length of concatenated substring
        n = len(s)

        # Frequency map of words
        from collections import Counter
        word_count = Counter(words)

        res = []

        # We check windows starting at offsets 0..w-1
        for offset in range(w):
            left = offset
            seen = Counter()
            count = 0  # how many words matched in current window

            # Slide window in steps of w
            for right in range(offset, n - w + 1, w):
                word = s[right:right + w]

                if word in word_count:
                    seen[word] += 1
                    count += 1

                    # If we used a word more times than allowed → shrink window
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + w]
                        seen[left_word] -= 1
                        left += w
                        count -= 1

                    # If exactly k words matched → valid index
                    if count == k:
                        res.append(left)

                        # Move window by removing 1 word from left
                        left_word = s[left:left + w]
                        seen[left_word] -= 1
                        left += w
                        count -= 1

                else:
                    # Reset window if invalid word encountered
                    seen.clear()
                    count = 0
                    left = right + w

        return res

        