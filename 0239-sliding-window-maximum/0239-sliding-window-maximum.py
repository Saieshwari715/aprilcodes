import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        ans=[]
        n=len(nums)
        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))
            while heap[0][1]<=i-k:
                heapq.heappop(heap)

            if i>=k-1:
                ans.append(-heap[0][0])
        return ans

'''        n=len(nums)
        for i in range(n-k+1):
            maxi=max(nums[i:k+i])
            nums[i]=maxi
        return nums[0:n-k+1]'''
        