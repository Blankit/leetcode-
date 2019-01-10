class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        """
        return s[::-1]

s ="A man, a plan, a canal: Panama"
A = Solution()
b = A.reverseString(s)
print b