class Solution:
    def maximumLengthSubstring(self, s):
        # Intuition: check every substring independently, count frequencies from scratch
        n = len(s)
        result = 0
        for left in range(n):
            for right in range(left, n):
                freq = [0] * 26
                valid = True
                for i in range(left, right + 1):
                    c = ord(s[i]) - ord('a')
                    freq[c] += 1
                    if freq[c] > 2:
                        valid = False
                        break
                if valid:
                    result = max(result, right - left + 1)
        return result