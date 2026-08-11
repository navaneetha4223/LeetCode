class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):
            return 1.0
        if(x == 0):
            return 0.0
        if(x == 1):
            return 1.0
        if(x == -1 and n % 2 == 0):
            return 1.0
        if(x == -1 and n % 2 != 0):
            return -1.0
        ans = 1
        if(n < 0):
            n = n * -1
            x = 1 / x
        binForm = n
        while(binForm > 0):
            if(binForm % 2 == 1):
                ans *= x
            x *= x
            binForm //= 2
        return ans