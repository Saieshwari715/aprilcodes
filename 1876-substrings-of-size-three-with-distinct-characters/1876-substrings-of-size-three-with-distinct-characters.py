class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            st=s[i:i+3]
            if len(set(st))==3:
                c+=1
        return c
        