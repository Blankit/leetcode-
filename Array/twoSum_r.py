#coding:utf-8
'''
问题：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''
"""
边遍历，边查找
前面将num存储起来，后面再target-num2==num时，就可以将该数取出了
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        i = 0
        j = i + 1
        dic = {}
        for index,num in enumerate(nums):
            # print index,num
            num2 = target - num
            if num2 in dic:
                return [dic[num2],index]
            else:
                dic[num] = index



nums = [3,2,4]
target = 6
A = Solution()
b = A.twoSum(nums,target)
print b
