class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        c1=c2=0
        v1=v2=None
        for num in nums:
            if num==v1:
                c1+=1
            elif num==v2:
                c2+=1
            elif c1==0:
                v1=num
                c1=1
            elif c2==0:
                v2=num
                c2=1
            else:
                c1-=1
                c2-=1
        arr=[]
        n=len(nums)
        if nums.count(v1)>n//3:
            arr.append(v1)
        if nums.count(v2)>n//3:
            arr.append(v2)
        return arr

