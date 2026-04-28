class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l=0
        s=list(s)
        while l<len(s):
            s[l:l+k]=reversed(s[l:k+l])

            l+=2*k
        return "".join(s)

        

        