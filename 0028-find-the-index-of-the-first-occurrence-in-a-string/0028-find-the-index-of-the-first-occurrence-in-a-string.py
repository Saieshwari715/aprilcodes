class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
        
            if needle==haystack[i:len(needle)+i]:
                return i
                break
            
        return -1

        