class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        return haystack.find(needle)


haystack = "aaaaa"
needle = "bba"
haystack = "hellolllll"
needle = "ll"
A = Solution()
b = A.strStr(haystack,needle)
print b