class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        k=len(s)
        w=""
        for i in words:
            w+=i
            if w==s:
                return True
            if len(w)>k:
                return False
        
        return False
