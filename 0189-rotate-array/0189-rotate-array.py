class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        temp=[0]*n
        k=k%n
        
        for i in range(n-k,n):
            temp[abs(n-k-i)]=nums[i]
        for i in range(n-k):
            temp[k+i]=nums[i]
        for i in range(n):
            nums[i]=temp[i]
        
        return nums













        