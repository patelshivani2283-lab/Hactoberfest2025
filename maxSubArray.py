class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        sum = 0
        for i in nums:
            sum = sum + i
            maxsum = max(sum, maxsum) 
            if(sum<0):
                sum = 0          
        return maxsum

        
