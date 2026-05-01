class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=start^goal
        return bin(a).count("1")
        