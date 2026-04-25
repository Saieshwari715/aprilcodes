class Solution:
    def compress(self, chars: List[str]) -> int:
        l=0
        s=0
        for r in range(len(chars)):
            if r==len(chars)-1 or chars[r]!=chars[r+1]:
                c=r-l+1
                chars[s]=chars[l]
                s+=1 
                if c>1:
                    for digit in str(c):
                        chars[s]=digit
                        s+=1
                l=r+1
        return s



        l=r+1

                

        
       