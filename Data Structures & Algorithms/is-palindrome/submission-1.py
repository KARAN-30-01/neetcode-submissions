class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and lowercase them
        s2 = "".join(char.lower() for char in s if char.isalnum())
        
        i = 0
        j = len(s2) - 1
        
        while i < j:
            if s2[i] != s2[j]:
                return False
            i += 1
            j -= 1
            
        return True
