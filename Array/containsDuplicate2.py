#coding:utf-8
'''
使用集合
1. 对原列表取集合
2. 若集合的长度与列表的长度相同，则列表无重复
3. 排除列表长度为0和1的情形
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l < 2:
            return False

        s = set(nums)
        s = len(s)
        if l == s:
            return False
        else:
            return True
nums = [1,2,3,1]
A = Solution()
b = A.containsDuplicate(nums)
print b
