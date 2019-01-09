class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        # if l<2:
        #     digits[0] += 1
        #     return
        flag = 1
        for i in range(l-1,-1,-1):
            temp = flag + digits[i]
            if temp >= 10:
                digits[i] = temp - 10
                flag = 1
            else:
                digits[i] = temp
                flag = 0
        if flag:
            digits.insert(0,flag)
        return digits



digits = [1,2,3]
digits = [9,9,9,9]
digits = [9]
A = Solution()
b = A.plusOne(digits)
print digits