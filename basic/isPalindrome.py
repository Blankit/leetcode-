#coding:utf-8
'''
1. 使用str.upper()将字母全变为大写
2. str.isalnum()过滤掉无效字符
3. flag1、flag2判断所取的元素是否是有效字符(官方给出的答案使用了continue)
4. 空字符串的长度为0、单个字符均为回文字符串

'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l <= 1:
            return True
        s = s.upper()
        i = 0
        j = l - 1
        flag1 = 0
        flag2 = 0
        while(i<j):
            if s[i].isalnum():
                pre = s[i]
                flag1 = 1

            else:
                i += 1
                flag1 = 0
            if s[j].isalnum():
                posterior = s[j]
                flag2 = 1
            else:
                j -= 1
                flag2 = 0
            if (flag1 & flag2):
                if pre == posterior:
                    i += 1
                    j -= 1
                else:
                    return False

        return True


s = "A man, a plan, a canal: Panama"
s = "race a car"
A = Solution()
b = A.isPalindrome(s)
print b
