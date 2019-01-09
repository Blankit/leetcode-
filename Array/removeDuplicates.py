#coding:utf-8
'''
维护一个无重复元素的数组，它的长度由i确定
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        l = len(nums)
        if l < 1:
            return
        for j in range(1,l):
            if nums[j]!= nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
A = Solution()
b = A.removeDuplicates(nums)
print b
print nums
