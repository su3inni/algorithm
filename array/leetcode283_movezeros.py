class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        switch=0
        search=0
        while(search<len(nums) and switch<len(nums)):
            if nums[search]!=0 and nums[switch]==0:
                nums[switch]=nums[search]
                nums[search]=0
                switch+=1
                search+=1
            elif nums[search]!=0 and nums[switch]!=0:
                search+=1
                switch+=1
            else:
                search+=1
