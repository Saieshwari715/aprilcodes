class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        wor=set(word)
        c=0
        for i in wor:
            if i.islower():
                if i.upper() in wor:
                    c+=1
        return c

        
        