#coding:utf-8
'''
1. 使用str.upper()将字母全变为大写
2. str.isalnum()过滤掉无效字符
3. flag1、flag2判断所取的元素是否是有效字符
4. 空字符串的长度为0、单个字符均为回文字符串
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.upper()
        s = filter(str.isalnum,s)
        l = len(s)
        i = 0
        j = l - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
s ="A man, a plan, a canal: Panama"
s = "race a car"
A = Solution()
b = A.isPalindrome(s)
print b