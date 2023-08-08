class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=sum(nums[1:])
        for i in range(len(nums)-1):
            if left_sum==right_sum : 
                return i 
            else:
                left_sum +=nums[i]
                right_sum-=nums[i+1]
        if sum(nums[:len(nums)-1])==0:
            return len(nums)-1
        return -1
