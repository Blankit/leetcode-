#coding:utf-8
'''
当n>2时，f(n) = f(n-1) + f(n-2)
但是递归的方法存在很耗时，存在大量的重复运算
使用两个变量存储中间值，来节省操作次数
感觉这里真的是方法用对了，可以提高效率
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=3:
            return n
        num1 = 1
        num2 = 2
        result = 0
        while n>2:
            result = num1 + num2
            num1 = num2
            num2 = result
            n -= 1
        return  result


n = 10
A = Solution()
b = A.climbStairs(n)
print b

