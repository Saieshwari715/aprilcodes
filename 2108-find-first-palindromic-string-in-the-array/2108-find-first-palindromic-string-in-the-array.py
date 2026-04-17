class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in words:
            f=True
            j,k=0,len(i)-1
            while j<k:
                if i[j]!=i[k]:
                    f=False

                    break
                j+=1
                k-=1
            
            if f:
                return i
        return ""
        