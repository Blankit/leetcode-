#coding:utf-8
'''
1. 排序后判断两个数组是否相等
2.分别构建字典，观察s中字符出现的次数与t中是否相等。
注意比较的时候使用set(s).
在比较时，要判断s中的字符在t中时候出现，否则直接判断会出现键值错误
3.使用s.count（）方法，比较每个字符出现的次数
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        if len(s)!= len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

s = "a"
t = "a"
A = Solution()
b = A.isAnagram(s,t)
print b