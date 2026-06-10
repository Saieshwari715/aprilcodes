class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub=s[i:j]
                
                nice=True
                for ch in sub:
                    if ch.swapcase() not in sub:
                        nice=False
                        break
                if nice and len(sub)>len(ans):
                    ans=sub

        return ans


        