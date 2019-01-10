class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        """
        s = list(s)
        # print s
        l = len(s)
        i = 0
        j = l - 1
        while i<j:
            if not s[i]:
                i +=1
            if not s[j]:
                j -= 1
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return ''.join(i for i in s)

s ="A man, a plan, a canal: Panama"
A = Solution()
b = A.reverseString(s)
print b