class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        w=set()
        for i in words:
            l=""
            for j in i:
                l+=d[ord(j)-97]
            w.add(l)
        return len(w)

        