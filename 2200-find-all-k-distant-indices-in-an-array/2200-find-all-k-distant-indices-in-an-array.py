class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a=[]
        i=0
        j=0
        while i<len(nums):
            while j<len(nums) and (nums[j]!=key or j<i-k):
                j+=1
            
            if j<len(nums) and abs(i-j)<=k:
                a.append(i)
            i+=1
            
        return sorted(a)

        