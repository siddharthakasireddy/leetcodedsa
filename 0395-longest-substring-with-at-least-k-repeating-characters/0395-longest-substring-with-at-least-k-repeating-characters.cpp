class Solution {
public:
    int longestSubstring(string s, int k) {
        return helper(s, 0, s.size(), k);
    }
    
    int helper(const string &s, int start, int end, int k) {
        if (end - start < k) return 0;

        int freq[26] = {0};
        for (int i = start; i < end; i++) {
            freq[s[i] - 'a']++;
        }

        for (int i = start; i < end; i++) {
            if (freq[s[i] - 'a'] < k) {
                int j = i + 1;
                while (j < end && freq[s[j] - 'a'] < k) j++;
                return max(
                    helper(s, start, i, k),
                    helper(s, j, end, k)
                );
            }
        }

        return end - start;  // Entire substring is valid
    }
};
