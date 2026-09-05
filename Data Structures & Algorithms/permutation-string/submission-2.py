class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def freqmap(s):
            hash1={}
            for i in s:
                hash1[i] = hash1.get(i,0)+1
            return hash1    
        
        s11 = freqmap(s1)
        s22 = freqmap(s2[0:len(s1)])
        i=1
        if s11 == s22:
                return True

        while i+len(s1)-1< len(s2):

            s22[s2[i-1]] -= 1

            if s22[s2[i-1]] == 0:
                del s22[s2[i-1]]

            s22[s2[i+len(s1)-1]] = s22.get(s2[i+len(s1)-1], 0) + 1

            i += 1

            if s11 == s22:
                return True
                
        return False
        