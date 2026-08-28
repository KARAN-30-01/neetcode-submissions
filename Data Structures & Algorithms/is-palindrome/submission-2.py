class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            # Skip non-alphanumeric characters from the left
            while i < j and not s[i].isalnum():
                i += 1
            # Skip non-alphanumeric characters from the right
            while i < j and not s[j].isalnum():
                j -= 1
                
            # Compare lowercase variants
            if s[i].lower() != s[j].lower():
                return False
                
            i += 1
            j -= 1
            
        return True
