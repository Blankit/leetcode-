#coding:utf-8
'''
1. 字符串不可更改内容。将字符串转成列表，结果转换完成后，转成字符串
2. 采用双指针
3.   s = ''.join(i for i in s)与s = ''.join(s)#当s是列表时，后者速度刚快
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = s.lower()
        l = len(s)
        if l <= 1:
            return s
        # s = list(s)
        # vowel = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
        vowel = 'aeiouAEIOU'  # 速度更快

        i = 0
        j = l - 1
        while (i < j):
            if s[i] not in vowel:
                i += 1
                continue
            if s[j] not in vowel:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        # s = ''.join(i for i in s)
        s = ''.join(s)#更快
        return s


s = "hello"
A = Solution()
b = A.reverseVowels(s)
print b

