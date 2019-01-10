class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= -1*pow(2,31) or x > pow(2,31):
            return 0
        while x:
            if not x % 10:
                x /= 10
            else:
                break
        if x<0:
            sign = -1
        else:
            sign = 1
        x *= sign
        r = []
        while x:
            r.append(x%10)
            x /= 10
        s = 0
        for i in r:
            s = s*10 + i
            if s <= -1 * pow(2, 31) or s > pow(2, 31):
                return 0
        return s*sign



x =1534236469
A = Solution()
b = A.reverse(x)
print b


