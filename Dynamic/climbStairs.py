import time

#递归
class Solution(object):
    def f(self,n):
        if n <3:
            return n
        else:
            return self.f(n-2)+self.f(n-1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        """
        return self.f(n)
n = 10
start = time.time()
A = Solution()
b = A.climbStairs(n)
print b
print time.time() - start

