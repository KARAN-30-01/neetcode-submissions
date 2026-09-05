class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t1 = {}

        for c in t:
            t1[c] = t1.get(c, 0) + 1

        s2 = {}

        l = 0
        r = 0

        have = 0
        need = len(t1)

        minlen = float('inf')
        best_l = 0
        best_r = 0

        while r < len(s):

            # Add right character
            s2[s[r]] = s2.get(s[r], 0) + 1

            # This character has now reached its required frequency
            if s[r] in t1 and s2[s[r]] == t1[s[r]]:
                have += 1

            # Window is valid
            while have == need:

                # Record smallest valid window
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    best_l = l
                    best_r = r

                # Remove left character
                if s[l] in t1 and s2[s[l]] == t1[s[l]]:
                    have -= 1

                s2[s[l]] -= 1
                l += 1

            r += 1

        if minlen == float('inf'):
            return ""

        return s[best_l:best_r + 1]