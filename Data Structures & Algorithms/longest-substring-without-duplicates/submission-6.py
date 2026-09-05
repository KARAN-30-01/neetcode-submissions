class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash1 = {}
        i = 0
        maxlen = 0

        for j in range(len(s)):
            if s[j] in hash1:
                i = max(i, hash1[s[j]] + 1)

            hash1[s[j]] = j
            maxlen = max(maxlen, j - i + 1)

        return maxlen