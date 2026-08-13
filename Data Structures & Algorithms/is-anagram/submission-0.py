class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def check(arr):
            freq = {}
            for i in arr:
                freq[i] = freq.get(i, 0) + 1
            return freq
        if check(s) == check(t):
            return True
        else:
            return False            

        