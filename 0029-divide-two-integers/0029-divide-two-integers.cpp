class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == divisor) return 1;

        long long ans = 0;
        int sign = 1;

        if ((dividend < 0 && divisor > 0) || 
            (dividend > 0 && divisor < 0))
            sign = -1;

        long long n = llabs((long long)dividend);
        long long d = llabs((long long)divisor);

        while (n >= d) {
            int count = 0;
            while (n >= (d << (count + 1)))
                count++;

            n -= d << count;
            ans += 1LL << count;
        }

        if (ans > INT_MAX && sign == 1) return INT_MAX;
        if (-ans < INT_MIN && sign == -1) return INT_MIN;

        return sign * ans;
    }
};