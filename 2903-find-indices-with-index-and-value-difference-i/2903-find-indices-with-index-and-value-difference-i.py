class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        
        for i in range(len(nums)):
            j=0
            while j<len(nums):
                if abs(nums[i]-nums[j])>=valueDifference and abs(i-j)>=indexDifference:
                    return [i,j]
                j+=1
        return [-1,-1]




        