#coding:utf-8
'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.
s = "loveleetcode",
返回 2.
'''
'''
用字符串的find和rfind方法。
find返回从左向右第一个查找到的字符串的下标，rfind是从右到左，第一个找到的字符的下标
若这两个值相等，表示在字符串中这个字符串只出现一次

'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphbet = 'abcdefghijklmnopqrstuvwxyz'
        s_length = len(s)
        p = s_length
        for i in alphbet:
            if s.find(i)!=-1 and s.find(i) == s.rfind(i):#找出只出现一次的字符
                p = min(p,s.find(i))#求p的最小值
        if p==s_length:#循环一次也没执行，p还是原值。如果只有一个元素或最后一个元素没重复，p = s_length -1
            return -1
        return p
s = "loveleetcode"
A = Solution()
b = A.firstUniqChar(s)
print b
