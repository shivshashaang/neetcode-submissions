class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        p2 = 1
        p1 = 2

        for i in range(3, n+1):
            temp = p1+p2
            p2 = p1
            p1 = temp
        return p1

