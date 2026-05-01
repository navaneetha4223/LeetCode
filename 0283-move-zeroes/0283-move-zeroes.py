class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        l=0
        for i in range(n):
            if nums[i] !=0:
                nums[l]=nums[i]
                l+=1
        for i in range(l,n):
            nums[i]=0
