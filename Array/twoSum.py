#coding:utf-8
'''
双指针的只能用于排好序的数组
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        i = 0
        j = l - 1


nums = [3,2,5]
target = 8
A = Solution()
b = A.twoSum(nums,target)
print b
