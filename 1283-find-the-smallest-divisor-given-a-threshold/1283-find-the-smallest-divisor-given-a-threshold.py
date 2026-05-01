from math import ceil
class Solution:
    def smallestDivisor(self,arr,k):
        low = 1
        high = max(arr)

        while (low <= high):
            mid = (low + high) // 2
            sum=0
            for num in arr:
                sum+=ceil(num/mid)
            if(sum<=k):
                high=mid-1
            else:
                low=mid+1
        return low