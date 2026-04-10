class Solution:
    def validPalindrome(self, s: str) -> bool:
        def fun(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        i=0
        j=len(s)-1
        c=0
        while i<=j:
            if s[i]!=s[j]:
                return fun(s,i+1,j) or fun(s,i,j-1)
            i+=1
            j-=1
        return True

        